from pathlib import Path
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot, row
from bokeh.models import Select
from bokeh.models.callbacks import CustomJS


data_path = r"E:\Studies\Data centric application development\data\data.csv"
df = pd.read_csv(data_path)

options = list(df.dtypes[df.dtypes == "float64"].index)

source = ColumnDataSource(df)

plot = figure(sizing_mode="stretch_both")
plot.xaxis.axis_label = "total_cases"
plot.yaxis.axis_label = "total_deaths"

scatter = plot.circle(x="total_cases", y="total_deaths", source=source,)

xfeature = Select(title="Select X axis Feature", options=options, value="total_cases")
yfeature = Select(title="Select Y axis Feature", options=options, value="total_deaths")


xfeature.js_on_change(
    "value",
    CustomJS(
        args=dict(xaxis=plot.xaxis[0], scatter=scatter, source=source),
        code="""
    scatter.glyph.x.field = cb_obj.value
    xaxis.axis_label = cb_obj.value
    source.change.emit()
    """,
    ),
)

yfeature.js_on_change(
    "value",
    CustomJS(
        args=dict(yaxis=plot.yaxis[0], scatter=scatter, source=source),
        code="""
    scatter.glyph.y.field = cb_obj.value
    yaxis.axis_label = cb_obj.value
    source.change.emit()
    """,
    ),
)

show(gridplot([[row(xfeature, yfeature)], [plot]]))
