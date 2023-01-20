## Getting started with the Lollapalooza dashboard

You should already have installed the libraries for this week from requirements.txt in the repository.

This activity is inspired by
a [tutorial on freecodecamp by Déborah Mesquita.](https://www.freecodecamp.org/news/how-and-why-i-used-plotly-instead-of-d3-to-visualize-my-lollapalooza-data-d48345e2ca68/)

Some code has been modified from the original article to fit with this activity. The data preparation activities have
been added to functions in a file called `prepare_data.py` to remove complexity from the exercises, since the focus of
this tutorial is to create charts and not to prepare data (data preparation was covered in COMP0035).

Explore the `lollapalooza_app` directory structure. This is the structure suggested in earlier teaching materials. There
is also a skeleton `dash_app.py` which you should use for this first activity.

Add imports for the necessary libraries to `dash_app.py`. You will need to import `pandas as pd` to create a dataframe,
and `plotly.express as px` to create the charts.

Check that you can run the Dash app before you start.

## Questions to be answered from the data set

For the 2018 edition of Lollapalooza Brazil, all purchases were made through an RFID-enabled wristband.

The author used the data to see what she could learn about her festival experience by analyzing the purchases made at
the festival.

The data includes:

- purchase date
- purchase hour
- product
- quantity
- stage
- place where the purchase was made

Based on this data, the questions to be answered are:

- How did she spend her money?
- Where did she go during the festival?
- Which concerts did she watch?  (this will be answered in the Intro to plotly go activity)

## How did she spend her money?

To answer this, create a bar chart with spend for food and beverage by each day and build a heatmap to show when she
bought stuff.

### Create a chart

To create a bar chart using Plotly Express you need to read the data into a data frame, carry out the preparation tasks
and then create a figure. Add the following code before creating the app and the app layout in Dash.

```python 
file_path = Path(__file__).parent.joinpath('data', 'purchase_data.csv')
df_purchase = pd.read_csv(file_path)
purchase_df = prepare_data.prepare_purchase_data(df_purchase)
fig_bar = px.bar(purchase_df, x="spend", y="date", color="place")
```

You now need to add a place for the chart to be displayed in the HTML page. To do this you use the dash core
components (`dcc`) and not HTML. For example:

```python
dcc.Graph(
    id='spend-bar-graph',
    figure=fig_bar
)
```

Stop and re-run the Dash app. You should see the chart displayed.

### Style a chart

There are the 4 ways you can style and customize figures made with Plotly Express:

1. Control common parameters like width & height, titles, labeling and colors using built-in Plotly Express function arguments.

Go to [this page](https://plotly.com/python/styling-plotly-express/#builtin-plotly-express-styling-arguments) and use
the guidance. Then modify the fig code to add `title="Purchases by place"` to the chart.

```python
fig_bar = px.bar(purchase_df, x="spend", y="date", color="place", title="Purchases by place")
```

2. Updating the figure attributes using [update methods or by directly setting attributes](https://plotly.com/python/creating-and-updating-figures/)

Read [the documentation here](https://plotly.com/python/creating-and-updating-figures/#adding-traces) - scroll a little
to the plotly express example.

The example in the documentation uses the `.add_trace()` method which uses plotly go which we haven't imported. You can
use the same update method principle to add a title and change the font size using the `.update_layout()`
method e.g. `fig.update_layout(title_text="Sample Dataset - Updated", title_font_size=20)`

```python
fig_bar = px.bar(purchase_df, x="spend", y="date", color="place")
fig_bar.update_layout(title="Purchases by place", title_font_size=20)
```

3. Using Plotly's [theming/templating mechanism](https://plotly.com/python/templates/) via the template argument to
   every Plotly Express function

   [Read the documentation on adding a theme to a plotly express chart](https://plotly.com/python/templates/#specifying-themes-in-plotly-express)
   to learn how to apply the template argument to every Plotly Express function

   Add the plotly_dark template to the chart.

4. Setting default values for common parameters using px.defaults

Read
the [documentation on setting styling defaults.](https://plotly.com/python/styling-plotly-express/#setting-plotly-express-styling-defaults)

Set the default template to plotly_dark, set the default height and width each to 500px.

## Add a heatmap to the Dash app

This uses the same initial dataframe as the purchases by place bar chart. The data is then prepared for the heatmap as
an image.

```python
heatmap_df = prepare_data.prepare_purchase_data_heatmap(df_purchase)
fig_heatmap = px.imshow(heatmap_df)
```

Add another chart element to the app layout:

```python
dcc.Graph(
    id='spend-heatmap',
    figure=fig_heatmap
),
```

## Add a map to answer 'Where did she go during the festival?'

"The data only tells us the name of the location where I made the purchase, and the festival took place at Autódromo de
Interlagos.

I took the map with the stages from here and used the georeferencer tool from georeference.com to get the latitude and
longitude coordinates for the stages.

We need to display a map and the markers for each purchase, so we will use Mapbox and the scattermapbox trace.

You will need to [generate a mapbox token from the mapbox site](https://www.mapbox.com/help/define-access-token/) and
then place your token in the first line of code after the import statements in the code below. You will need to create
an account to do this. If you don't feel comfortable in signing up then you can skip this chart."

The following code creates the chart:

```python
file_path_stages = Path(__file__).parent.joinpath('data', 'stages.csv')
df_stages = pd.read_csv(file_path_stages)

mapbox_token = "" # Add your mapbox token here
px.set_mapbox_access_token(mapbox_token)

fig_map = px.scatter_mapbox(df_stages,
                            lat="latitude",
                            lon="longitude",
                            color="stage",
                            center=dict(lat=-23.701057, lon=-46.6970635),
                            hover_name="stage",
                            zoom=14.5,
                            title='Lollapalooza Brazil 2018 map')
```

Now add the chart to the Dash app layout. Add a suitable html.H2 heading above it. 

## Adding plotly go charts to the Lollapalooza dashboard

Plotly Go is covered in a later week. However you can attempt this now if you wish.

## Add a map to answer 'Where did she go during the festival?'

"The data only tells us the name of the location where I made the purchase, and the festival took place at Autódromo de Interlagos.

I took the map with the stages from here and used the georeferencer tool from georeference.com to get the latitude and longitude coordinates for the stages.

We need to display a map and the markers for each purchase, so we will use Mapbox and the scattermapbox trace.

You will need to [generate a mapbox token from the mapbox site](https://www.mapbox.com/help/define-access-token/) and
then place your token in the first line of code after the import statements in the code below. You will need to create
an account to do this. If you don't feel comfortable in signing up then you can skip this chart."

```python
mapbox_token = ""  # Add your mapbox token here

df = pd.read_csv("../data/stages.csv")

trace = go.Scattermapbox(
   lat=df["latitude"], 
   lon=df["longitude"], 
   text=df["stage"],
   marker={'size': 12},
   mode="markers+text",
   textposition="top left"
   )

data = [trace]

layout = go.Layout(mapbox=dict(accesstoken=mapbox_token, center=dict(lat=-23.701057, lon=-46.6970635), zoom=14.5))

figure = go.Figure(data=data, layout=layout)

```

## Add a table to guess the concerts she attended based only on purchases

"Ideally, when we are watching a show, we are watching the show (and not buying stuff), so the purchases should be made before or after each concert. I then made a list of each concert happening one hour before, one hour after, and according to the time the purchase was made.

To find out which one of these shows I attended, I calculated the distance from the location of the purchase to each stage. The shows I attended should be the ones with the shortest distance to the concessions.

As we want to show each data point, the best choice for a visualization is a table."

The data file is `data/concerts_I_attended.csv`

The code to prepare the data is in the function `prepare_data.prepare_concert_data(df)`

Add the code to create the figure using the data from the data file to `dash_app.py`.

```python
file_path_concert = Path(__file__).parent.joinpath('data', 'concerts_I_attended.csv')

df_table = pd.read_csv(file_path_concert)

df_table = prepare_data.prepare_concert_data(df_table)

trace_table = go.Table(
   header=dict(
      values=["Concert", "Date", "Correct?"], 
      fill=dict(color=("rgb(82,187,47)"))),
   cells=dict(
      values=[df_table.concert, df_table.date, df_table.correct],
      font=dict(color=([df_table.color])))
   )

data = [trace_table]

fig_table = go.Figure(data=data)
```

Write the code to create the table in the app layout.

Re-run the Dash app.