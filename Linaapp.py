from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_URL = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.0686/lat/59.3293/data.json"

def get_temperature():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        
        for time_series in data.get('timeSeries', []):
            for param in time_series.get("parameters", []):
                if param['name'] == 't':  # Temperatur
                    return param["values"][0]
        return None
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None

@app.route('/')
def index():
    temperature = get_temperature()
    if temperature is not None:
        return render_template('index.html', temperature=temperature)
    else:
        return "Failed to fetch temperature data."

@app.route('/api/temperature')
def temperature_api():
    temperature = get_temperature()
    return jsonify({"temperature": temperature})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
