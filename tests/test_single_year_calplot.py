from datetime import datetime
from unittest import TestCase

import pandas as pd
from plotly import graph_objects as go
from plotly.subplots import make_subplots

from plotly_calplot.single_year_calplot import year_calplot


class TestSingleYearCalplot(TestCase):
    defaults = {
        "name": "y",
        "text_name": None,
        "dark_theme": False,
        "month_lines": True,
        "month_lines_width": 1,
        "month_lines_color": "#9e9e9e",
        "top_bottom_lines": True,
        "gap": 1,
        "colorscale": "greens",
        "title": "",
        "total_height": None,
        "text": None,
        "years_as_columns": False,
        "start_month": 1,
        "end_month": 12,
        "hovertemplate": None,
        "customdata": None,
    }

    def setUp(self) -> None:
        self.sample_dataframe = pd.DataFrame(
            [
                (datetime(2019, 1, 1), 13),
                (datetime(2019, 1, 1), 16),
                (datetime(2019, 1, 3), 5),
                (datetime(2019, 3, 31), 2),
                (datetime(2019, 4, 1), 27),
                (datetime(2019, 4, 2), 29),
                (datetime(2019, 4, 3), 20),
                (datetime(2019, 4, 4), 13),
                (datetime(2019, 4, 5), 23),
                (datetime(2019, 5, 30), 0),
            ],
            columns=["ds", "value"],
        )

    def test_should_create_single_year_calplot(self) -> None:
        fig = make_subplots(1, 1)
        cp = year_calplot(self.sample_dataframe, "ds", "value", fig, 0, 2019, **self.defaults)
        self.assertTrue(type(cp) == go.Figure)
