from flask import Flask
import requests
from datetime import datetime

app = Flask(name)

@app.route("/")
def fetchweather():

    apiurl = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.0686/lat/59.3293/data.json"
    headers = {
        "Accept": "application/json",
        "User-Agent": "weather-app",
    }
    response = requests.get(apiurl, headers=headers)
    if response.statuscode == 200:
        data = response.json()
        time_series = data["timeSeries"][0]
        parameters = time_series["parameters"]

        temperature = None
        for param in parameters:
            if param["name"] == "t":
                temperature = f"{param['values'][0]} C"
                break

        if temperature:
            result = f"""
            <h2><strong>Data fetched at Stockholm</strong></h2>
            <strong>Temperature:</strong> {temperature}<br>
            """
        else:
            result = "Temperature data from SMHI is not available."

        return result

    else:
        return "Failed to fetch data from SMHI API", response.status_code

if __name == "__main":
    app.run(host="0.0.0.0", port=80)

