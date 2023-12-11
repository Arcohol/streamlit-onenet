import streamlit as st
import altair as alt
from utils import *

st.title("OneNET Demo")

st.header(":earth_asia: Overview (Latest Values)")

col1, col2 = st.columns(2)
col1.metric("Temperature", get_latest_datapoint("temp") + " °C")
col2.metric("Humidity", get_latest_datapoint("hum") + " %")

st.header(":chart_with_upwards_trend: Charts")

with st.container(border=True):
    temp = get_datapoints("temp", limit=50)
    c = (
        alt.Chart(temp)
        .mark_line(point=True)
        .encode(x="Time", y="Value", tooltip=["Time", "Value"])
        .interactive()
    )
    st.subheader("Temperature")
    temp_chart = st.altair_chart(c, use_container_width=True)

    hum = get_datapoints("hum", limit=50)
    c = (
        alt.Chart(hum)
        .mark_line(point=True)
        .encode(x="Time", y="Value", tooltip=["Time", "Value"])
        .interactive()
    )
    st.subheader("Humidity")
    hum_chart = st.altair_chart(c, use_container_width=True)
