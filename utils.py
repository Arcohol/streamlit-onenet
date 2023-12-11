import requests
import pandas as pd
from streamlit import secrets

DEVICE_ID = secrets["DEVICE_ID"]
API_KEY = secrets["API_KEY"]


def get_datapoints(datastream, limit=20):
    url = f"https://api.heclouds.com/devices/{DEVICE_ID}/datapoints?datastream_id={datastream}&limit={limit}"
    headers = {"api-key": API_KEY}
    r = requests.get(url, headers=headers).json()

    timestamps = []
    values = []
    for point in r["data"]["datastreams"][0]["datapoints"]:
        # if point["value"] is not a valid float, skip it
        try:
            float(point["value"])
        except ValueError:
            continue

        timestamps.append(point["at"])
        values.append(float(point["value"]))

    df = pd.DataFrame({"Time": pd.to_datetime(timestamps), "Value": values})
    df.set_index("Time")
    return df


def get_latest_datapoint(datastream):
    url = f"https://api.heclouds.com/devices/{DEVICE_ID}/datastreams/{datastream}"
    headers = {"api-key": API_KEY}
    r = requests.get(url, headers=headers).json()
    return r["data"]["current_value"]


if __name__ == "__main__":
    d = get_latest_datapoint("temp")
    print(d)
