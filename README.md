# Calendar Heatmap with Plotly
Making it easier to visualize and costumize time relevant or time series data with plotly interaction.

## Changes in this fork

- Added this fork info
- Open up plotly dependency to `>=5.4.0` (might causes issues in the future with new plotly versions)
- Fix small details (type hints, ...)
- Include skip_empty_years from [juan11iguel/plotly-calplot](https://github.com/juan11iguel/plotly-calplot)
- Add option to replace NaN with zeros
- Add poethepoet as task runner


## Description

New to the library? Read [this Medium article](https://medium.com/@brunorosilva/5fc322125db7).

This plot is a very similar to the contribuitions available on Github and Gitlab profile pages and to [Calplot](https://github.com/tomkwok/calplot) - which is a pyplot implementation of the calendar heatmap, thus it is not interactive right off the bat.

The first mention I could find of this plot being made with plotly was in [this forum post](https://community.plotly.com/t/colored-calendar-heatmap-in-dash/10907/16) and it got my attention as something that should be easily available to anyone.

# Installation
``` bash
pip install plotly-calplot
```

# Examples

In [this Medium article](https://medium.com/@brunorosilva/5fc322125db7) I covered lot's of usage methods for this library.
``` python
from plotly_calplot import calplot

fig = calplot(df, x="date", y="value")
fig.show()
# you can also adjust layout and your usual plotly stuff
```

<img src="https://github.com/brunorosilva/plotly-calplot/blob/main/assets/images/example.png?raw=true">
