# Creating charts with Plotly Express and adding them to a Dash app

The following activities are expected to take 2 hours to complete.

## Introduction to Plotly Express

[Plotly Express](https://plotly.com/python/plotly-express/) is a high level API for creating charts using Python. By
high level, we mean that much of the complexity of the code required to create a chart is hidden from you and provided by the API, allowing you to create charts with less code.

Plotly express is a module in the plotly Python package, though it used to be a separate package. Install [plotly Python version](https://plotly.com/python/getting-started/) using `pip install plotly`.

The [online documentation](https://plotly.com/python/plotly-express/#highlevel-features) gives lots of examples of how to create different chart types. You will need to make use of this.

The [Plotly community forum](https://community.plotly.com/) has posts you can search; and you can post your own questions.

The current version of Plotly.py at the time of writing this is 5.11. Some examples you may find online are from much earlier versions and the code is likely to need to be adapted to work with the current version.

### Create a chart using Plotly Express

In this activity you will create a line chart to answer the question 'How has the number of sports in the summer and winter paralympics changed over time?'.

Assume that the target audience is university students interested in major sporting events. Assume they have limited knowledge of the paralympics however they make extensive use of a range of technologies and are capable of understanding more complex data and charts. The activity doesn't explicitly design for this audience but you may wish to try to do so.

The data is in the events.csv. The columns you will need are: ['REF', 'TYPE', 'YEAR', 'LOCATION', 'EVENTS', 'SPORTS', 'COUNTRIES', 'MALE', 'FEMALE', 'PARTICIPANTS']

First, check you can run the paralympics_app code. In the VS Code terminal: `python paralympics_app/paralympics.py`

#### Create a basic line chart

The steps are:

1. Use pandas to read the data into a dataframe
2. Create a line chart using the Plotly Express line chart function and the data
3. Add the chart to the Dash app using the dash core components Graph function

You can either add all the code to `paralympics.py`, or you may prefer to add the code to create the charts to a separate python file, e.g. called `create_charts.py`.

1. Use pandas to read the data into a dataframe

```python
from pathlib import Path
import pandas as pd


EVENT_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'events.csv')
cols = ['REF', 'TYPE', 'YEAR', 'LOCATION', 'EVENTS', 'SPORTS', 'COUNTRIES', 'MALE', 'FEMALE', 'PARTICIPANTS']
df_events = pd.read_csv(EVENT_DATA_FILEPATH, usecols=cols)
```

2. Create a line chart using the Plotly Express line chart function and the data

Refer to the [Plotly Express line chart guide](https://plotly.com/python/line-charts/).

The minimum needed to create a line chart is x, y and the dataframe.

```python
line_events = px.line(df_events,
                          x='YEAR',
                          y='EVENTS',
                          )

```

3. Add a dash core components graph component (dcc.Graph) to the Dash app layout. This makes the chart visible in the dashboard.

Refer to the example in [Plotly Dash layout documentation](https://dash.plotly.com/layout).

In `paralympic_app.py` in the `app.layout` code section add the figure as a dash core components graph (`dcc.Graph()`). 

Provide values for the `id` and `figure` parameters. 

The `id` isn't strictly necessary to display the chart now, however you will need it when we move on to adding interactivity next week so it is a good habit to create one. Remember that `id` must be unique on any given HTML document (web page). 

The value for `figure` should be the name of the variable that creates the line chart.

```python
app.layout = dbc.Container(
    [
        html.H1("Paralympic Medals Dashboard"),
        html.H2("Has the number of athletes, nations, events and sports changed over time?"),
        dcc.Graph(
            id='line-sports',
            figure=line_events
        ),
# existing code here....
```

4. Run the Dash app.

Dash includes "hot-reloading", this features is activated by default when you run your app withapp.run_server(debug=True). This means that Dash will automatically refresh your browser when you make a change in your code.

Update your `paralympics.py` code, the following will be towards the end of the file:

```python
if __name__ == '__main__':
    app.run_server(debug=True)
```

Run the app by entering the following in the VS Code terminal.

```
python paralympics_app/paralympics.py
```

#### Styling the chart

Refer to [Styling figures with Plotly Express](https://plotly.com/python/styling-plotly-express/).

There are the 4 ways you can style and customize figures made with Plotly Express:

1. Control common parameters like width & height, titles, labeling and colors using built-in Plotly Express function arguments.
2. Updating the figure attributes using [update methods](https://plotly.com/python/styling-plotly-express/#updating-or-modifying-figures-made-with-plotly-express).
3. Using Plotly's theming/templating mechanism via the template argument to every Plotly Express function. [The documentation explains how to add a theme to a plotly express chart](https://plotly.com/python/templates/#specifying-themes-in-plotly-express).
4. Setting [default values for common parameters using px.defaults](https://plotly.com/python/styling-plotly-express/#setting-plotly-express-styling-defaults)

The default chart style doesn't really adhere to the design principles. Let's apply the following changes using the methods above.

1. Some of the 'non-data ink' such as grid lines, background colours could be removed by using the simple_white [theme](https://plotly.com/python/templates/#specifying-themes-in-plotly-express).

All Plotly Express functions accept a `template=` argument that can be set to the name of a registered theme.

Add `template="simple_white"` as an argument to the code that creates the line chart.

The app should update the chart dynamically if you modified the run function with debug=True, if not then you may need to stop and restart the app in VS Code terminal.

2. You may need to add some non-data ink to avoid misleading as the peak in 1984 was due to the fact that the summer games were held in two locations which increased the number of events and participants as they are counted for each of the two events. Use the method of updating the figure to add an annotation.

You can use the following syntax:

```python
fig.add_annotation( # add a text callout with arrow
    text="below target!", 
    x="Fri", 
    y=400, 
    arrowhead=1, 
    showarrow=True
)
```

You will need to replace some of the values as follows:

```text
fig -> line_events
text="1984 held in New York & Stoke Mandeville"
x=1984
y = 1000
```

> Now try and create a line chart showing the number of participants rather than events.

#### Create a bar chart

Create a stacked bar chart to show whether the ratio of male and female athletes has changed over time for
the winter paralympics. This aims to answer the question "Has the ratio of male and female athletes changed over time?".

Steps:

1. Create the chart

This requires some manipulation of the dataframe contents.

You will need to these columns from the `paralympics.csv` file: `['TYPE', 'YEAR', 'LOCATION', 'MALE', 'FEMALE', 'PARTICIPANTS']`

Add two new columns to the dataframe that contains the result of calculating the % of male and female participants e.g. `df_events['M%'] = df_events['MALE'] / df_events['PARTICIPANTS']`

Create a new dataframe with only the values for the Winter olympics e.g. `df_gender = df_events.loc[df_events['TYPE'] == "Winter"]`

Sort the values by Year ascending using the `df.sort_values()` function. `df_gender = df_gender.sort_values(['YEAR'], ascending=(True))`

Create a new column that combines Location and Year to use as the x-axis labels e.g. `df_gender['xlabel'] = df_gender['LOCATION'] + ' ' + df_gender['YEAR'].astype(str)`

Create the figure e.g. `fig = px.bar()`. See [Plotly documentation](https://plotly.com/python/bar-charts/#bar-chart-with-plotly-express). You can pass multiple columns to the `y=` parameter, e.g. `y=['M%', 'F%']`

2. Add a `dcc.Graph` element to the app.layout section of the code to display the chart you created. Remember to add an `id`.

3. Re-run the Dash app (if it doesn't automatically update).

4. Style the chart.

As before the default styling could be improved. Investigate the [styling options](https://plotly.com/python/styling-plotly-express/) to achieve the following:

- Remove the y-axis title.
- Remove the x-axis title 'xlabel'.
- Add a title to show this is the Winter paralympics.
- Remove the tick lines from the x-axis. Hint `.update_xaxes`
- Remove the tick lines and the labels from the y-axis. Hint `.update_yaxes`

Try and do this yourself, if you get stuck there is a potential solution in week 3.

> Now try and add a second chart to show the same for the summer olympics.


#### Create a map-based chart

Create a [scatter mapbox](https://plotly.github.io/plotly.py-docs/generated/plotly.express.scatter_mapbox.html) using Plotly Express to answer the question "Where in the world have the Paralympics have been held?".

For this you can adapt the [OpenStreetMap tiles example](https://plotly.com/python/mapbox-layers/#openstreetmap-tiles-no-token-needed) in the Plotly documentation. This does not require a token. Some mapbox solutions require a (free) 

The example given in the Plotly documentation is:

```python
import pandas as pd

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, 
lat="lat", 
lon="lon", 
hover_name="City", 
hover_data=["State", "Population"],
color_discrete_sequence=["fuchsia"], 
zoom=3, 
height=300,
mapbox_style="open-street-map"
)

# The following sets zero margin around the mapbox chart. Try delete/comment out the following line and see the effect.
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

```

Create dataframe using the following columns from `paralympics.csv`:  `['TYPE', 'YEAR', 'LOCATION', 'LAT', 'LON', 'PARTICIPANTS']`

By now you should be able to work out the general steps to create a chart and add it to the app.layout.

Follow the example code above replacing it with the paralympics event data.

Pass the relevant column names to `lat='LAT'`, `lon='LON'`, `hover_name='LOCATION`.

Change the `hover_data=` to the columns you wish to be displayed.

Change zoom to `zoom=1`.

Delete the `height=300` parameter.

View the chart.

Try and alter the styling:

- Set the size of the marker to the number of participants using 'size='.
- Change the height and width of the chart so by default you see all of the world countries
- Change the mapbox style to 'stamen-terrain'
- Change the colour of the marker dots. Use [HTML color names](https://www.w3schools.com/colors/colors_names.asp) or [HEX codes](https://www.w3schools.com/colors/colors_hexadecimal.asp).

## Further practice

Re-create lollapoolza charts using the [activities/covid_dashboard.md](activities.md)

Create your own covid dashboard app (see [activities/covid.md](covid.md)).

Explore the [Plotly Express documentation](https://plotly.com/python/plotly-express/#highlevel-features) and try adding some other chart types, either to create standalone figures or add them to one of your existing Dash apps.