import os
import streamlit.components.v1 as components


_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "streamlit_location", url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_location", path=build_dir)


DEFAULT_LOCATION_RESULT = {
    "latitude": None,
    "longitude": None,
    "accuracy": None,
    "speed": None,
    "altitude": None,
    "altitudeAccuracy": None,
    "err": None
}

DEFAULT_PATTERN = [100]

def location(key=None):
    component_value = _component_func(key=key, default=None, method_intent="location")
    return DEFAULT_LOCATION_RESULT if component_value is None else component_value


def watch(enable_high_accuracy=False, timeout=36_00_000, maximum_age=0, key=None):
    component_value = _component_func(
        enableHighAccuracy=enable_high_accuracy,
        timeout=timeout,
        maximumAge=maximum_age,
        key=key,
        default=None,
        method_intent="watch",
    )
    return DEFAULT_LOCATION_RESULT if component_value is None else component_value

def vibrate(pattern=None, key=None):
    _component_func(pattern=DEFAULT_PATTERN if pattern is None else pattern, key=key, default=None, method_intent="vibrate")


if not _RELEASE:
    import pydeck as pdk
    import streamlit as st
    import pandas as pd

    current_location = watch(enable_high_accuracy=True)
    st.write(current_location)

    lon = current_location["longitude"]
    lat = current_location["latitude"]

    df = pd.DataFrame({"longitude": [lon], "latitude": [lat]})
    st.write(df)

    if current_location != DEFAULT_LOCATION_RESULT:
        vibrate()
        layer = pdk.Layer(
            "HeatmapLayer",
            data=df,
            get_position=["longitude", "latitude"],
        )

        view_state = pdk.ViewState(longitude=lon, latitude=lat, zoom=13)

        # Render
        r = pdk.Deck(layers=[layer], initial_view_state=view_state)
        st.pydeck_chart(r)
