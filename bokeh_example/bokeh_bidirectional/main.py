from pathlib import Path
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot, row
from bokeh.models import Select
from bokeh.io import curdoc


data_path = r"E:\Studies\Data centric application development\data\data.csv"
df = pd.read_csv(data_path)
options = list(df.dtypes[df.dtypes == "float64"].index)

source = ColumnDataSource(df)

plot = figure(sizing_mode="stretch_both", name="scatterplot")
plot.xaxis.axis_label = "total_cases"
plot.yaxis.axis_label = "total_deaths"

scatter = plot.circle(x="total_cases", y="total_deaths", source=source,)

xfeature = Select(title="Select X axis Feature", options=options, value="total_cases")
yfeature = Select(title="Select Y axis Feature", options=options, value="total_deaths")

def on_change_x(attr, old, new):
    scatter.glyph.x = new
    plot.xaxis.axis_label = new

def on_change_y(attr, old, new):
    scatter.glyph.y = new
    plot.yaxis.axis_label = new

# set callbacks
xfeature.on_change("value", on_change_x)
yfeature.on_change("value", on_change_y)

# get current doc ( Bokeh's representation that's in sync with JS )
doc = curdoc()

# add this grid plot to current document
doc.add_root(gridplot([[row(xfeature, yfeature)], [plot]]))