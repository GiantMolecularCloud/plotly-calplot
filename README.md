# Calendar Heatmap with Plotly
Making it easier to visualize and costumize time relevant or time series data with plotly interaction.

## updates in this fork

- Added this fork info
- Open up plotly dependency to `>=5.4.0` (might causes issues in the future with new plotly versions)
- Fix small details (type hints, remove double defaults)
- Include skip_empty_years from [juan11iguel/plotly-calplot](https://github.com/juan11iguel/plotly-calplot)
- Add option to replace NaN with zeros
- Add poethepoet as task runner
- Add option to show dates without entries as `0` instead of `NaN`
- Add option `top_bottom_lines` to display the same lines that separate months also at the top and bottom. With `month_lines`, this fully encloses months (like in [calplot](https://calplot.readthedocs.io/en/latest/index.html)) and makes it much more appealing visually.
- Also show line at end of last month, when option `month_lines` is enabled.
- Allow to set hovertemplate and customdata. Note that this can be a bit fiddly to get to work exactly how you want it.

**Updated plotly-calplot**
<img src="https://github.com/giantmolecularcloud/plotly-calplot/blob/main/assets/images/example_updated.png?raw=true">

<details>
<summary>Code of the updated example</summary>

```python
from datetime import datetime
import pandas as pd
import numpy as np
from plotly_calplot import calplot

df = pd.DataFrame(
    [
        (datetime(2019, 1, 1), 3, "a new year"),
        (datetime(2019, 1, 1), 6, "same day"),
        (datetime(2019, 1, 3), 5, "a third day"),
        (datetime(2019, 3, 31), 2, "end of march"),
        (datetime(2019, 4, 1), 7, "start of april"),
        (datetime(2019, 4, 2), 9, "april continues"),
        (datetime(2019, 4, 3), 2, "another day in april"),
        (datetime(2019, 4, 4), 1, "and again in april"),
        (datetime(2019, 4, 5), 3, "still in april"),
        (datetime(2019, 5, 30), 1, "end of may"),
        (datetime(2019, 9, 5), 4, "Custom hovertext"),
    ],
    columns=["date", "value", "note"],
)

fig = calplot(
    df, 
    x="date",
    y="value",
    colorscale="blues",
    years_title=True,
    replace_nans_with_zeros=True,
    cmap_min=0,
    hovertemplate = "<b>%{customdata[0]|%d %B %Y}</b><br>Value: %{z}<br>%{customdata[3]}",
    customdata = np.stack((df.date.astype(str), df.value.astype(str), df.note.astype(str)), axis=-1),
)
```

</details>


**Original plotly-calplot**
<img src="https://github.com/giantmolecularcloud/plotly-calplot/blob/main/assets/images/example_original.png?raw=true">

<details>
<summary>Code of the original example</summary>

```python
from datetime import datetime
import pandas as pd
import numpy as np
from plotly_calplot import calplot

df = pd.DataFrame(
    [
        (datetime(2019, 1, 1), 3, "a new year"),
        (datetime(2019, 1, 1), 6, "same day"),
        (datetime(2019, 1, 3), 5, "a third day"),
        (datetime(2019, 3, 31), 2, "end of march"),
        (datetime(2019, 4, 1), 7, "start of april"),
        (datetime(2019, 4, 2), 9, "april continues"),
        (datetime(2019, 4, 3), 2, "another day in april"),
        (datetime(2019, 4, 4), 1, "and again in april"),
        (datetime(2019, 4, 5), 3, "still in april"),
        (datetime(2019, 5, 30), 1, "end of may"),
        (datetime(2019, 9, 5), 4, "Custom hovertext"),
    ],
    columns=["date", "value", "note"],
)

fig = calplot(
    df, 
    x="ds",
    y="value",
    colorscale="blues",
    years_title=True,
    replace_nans_with_zeros=False,
    top_bottom_lines=False,
)
```
</details>


## Original description

New to the library? Read [this Medium article](https://medium.com/@brunorosilva/5fc322125db7).

This plot is a very similar to the contribuitions available on Github and Gitlab profile pages and to [Calplot](https://github.com/tomkwok/calplot) - which is a pyplot implementation of the calendar heatmap, thus it is not interactive right off the bat.

The first mention I could find of this plot being made with plotly was in [this forum post](https://community.plotly.com/t/colored-calendar-heatmap-in-dash/10907/16) and it got my attention as something that should be easily available to anyone.

### Installation
``` bash
pip install plotly-calplot
```

### Examples

In [this Medium article](https://medium.com/@brunorosilva/5fc322125db7) I covered lot's of usage methods for this library.
``` python
from plotly_calplot import calplot

fig = calplot(df, x="date", y="value")
fig.show()
# you can also adjust layout and your usual plotly stuff
```

<img src="https://github.com/brunorosilva/plotly-calplot/blob/main/assets/images/example.png?raw=true">
