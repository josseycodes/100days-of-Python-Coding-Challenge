from flask import Flask, render_template
from flask_socketio import SocketIO
import requests
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

# Replace these with your actual API keys and stock symbols
STOCK_API_KEY = 'your_alpha_vantage_api_key'
WEATHER_API_KEY = 'your_openweather_api_key'
STOCK_SYMBOL = 'AAPL'
WEATHER_CITY = 'London'

def fetch_stock_price():
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_SYMBOL}&interval=1min&apikey={STOCK_API_KEY}'
    response = requests.get(url)
    data = response.json()
    time_series = data.get('Time Series (1min)', {})
    latest_time = sorted(time_series.keys())[0]
    latest_data = time_series[latest_time]
    return latest_data['1. open']

def fetch_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={WEATHER_CITY}&appid={WEATHER_API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data['main']['temp']

def background_thread():
    while True:
        stock_price = fetch_stock_price()
        weather = fetch_weather()
        socketio.emit('update_data', {'stock_price': stock_price, 'weather': weather})
        time.sleep(60)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=background_thread).start()
    socketio.run(app, debug=True)
