from flask import Flask, make_response, jsonify, request
from weather import getWeather
import requests
import config as cfg
config = cfg.get_config()

app = Flask(__name__)

def get_suggestion(context):
    url = config['suggestion_app']  
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "context": context
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['answer']  
    
@app.route('/health', methods=['GET'])
def healthcheck():
    return make_response(jsonify({'status': 'healthy'}), 200)

@app.route('/', methods=['GET'])
def main():
    return app.send_static_file('main.html')

@app.route('/<filename>', methods=['GET'])
def static_files(filename):
    return app.send_static_file(filename)

@app.route('/get_weather', methods=['GET'])
def get_weather():
    zip = request.args.get('zip')
    weather = getWeather(zip)
    context = weather.verbal_weather()
    # answer = get_suggestion(context)
    answer = 'no model yet available'
    report = weather.weather_report()
    report['suggestion'] = answer
    return jsonify(report)

app.run(debug=True, host="0.0.0.0", port="8080")

    
    