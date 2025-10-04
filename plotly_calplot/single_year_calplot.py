"""Module for creating a single year calplot and adding it to a subplot figure."""

from typing import List, Optional

import numpy as np
from pandas.core.frame import DataFrame
from plotly import graph_objects as go

from plotly_calplot.date_extractors import get_date_coordinates, get_month_names
from plotly_calplot.layout_formatter import (
    create_month_lines,
    create_top_bottom_lines,
    decide_layout,
    update_plot_with_current_layout,
)
from plotly_calplot.raw_heatmap import create_heatmap_without_formatting


def year_calplot(
    data: DataFrame,
    x: str,
    y: str,
    fig: go.Figure,
    row: int,
    year: int,
    name: str,
    dark_theme: bool,
    month_lines: bool,
    month_lines_width: int,
    month_lines_color: str,
    top_bottom_lines: bool,
    gap: int,
    colorscale: str | list[tuple[int, str]],
    title: str,
    total_height: int | None,
    text: Optional[List[str]],
    text_name: Optional[str],
    years_as_columns: bool,
    start_month: int,
    end_month: int,
    hovertemplate: str | None,
    customdata: np.ndarray | None,
) -> go.Figure:
    """
    Each year is subplotted separately and added to the main plot.

    For more information, see the documentation of calplot().
    Parameters are virtually identical.
    """
    month_names = get_month_names(data, x, start_month, end_month)
    month_positions, weekdays_in_year, weeknumber_of_dates = get_date_coordinates(data, x)

    # the calendar is actually a heatmap :)
    cplt = create_heatmap_without_formatting(
        data,
        x,
        y,
        weeknumber_of_dates,
        weekdays_in_year,
        gap,
        year,
        colorscale,
        name,
        text=text,
        text_name=text_name,
        hovertemplate=hovertemplate,
        customdata=customdata,
    )

    if month_lines:
        cplt = create_month_lines(
            cplt,
            month_lines_color,
            month_lines_width,
            data[x],
            weekdays_in_year,
            weeknumber_of_dates,
        )

    if top_bottom_lines:
        cplt = create_top_bottom_lines(
            cplt,
            month_lines_color,
            month_lines_width,
            weeknumber_of_dates,
        )

    layout = decide_layout(dark_theme, title, month_names, month_positions)
    fig = update_plot_with_current_layout(fig, cplt, row, layout, total_height, years_as_columns)

    return fig
