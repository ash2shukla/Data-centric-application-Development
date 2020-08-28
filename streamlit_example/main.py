import streamlit as st
from pathlib import Path
import pandas as pd
from bokeh.plotting import figure

# data_path = r"E:\Studies\Data centric application development\data\data.csv"
data_path = "/data/data.csv"
df = pd.read_csv(data_path)
options = list(df.dtypes[df.dtypes == "float64"].index)

xfeature = st.sidebar.selectbox("Select X Axis Feature", options)
yfeature = st.sidebar.selectbox("Select Y Axis Feature", options)

plot = figure(sizing_mode="stretch_width")
plot.xaxis.axis_label = xfeature
plot.yaxis.axis_label = yfeature

plot.circle(x=xfeature, y=yfeature, source=df)
st.bokeh_chart(plot)
