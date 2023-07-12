import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = json.loads(response.text)
        return data
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

def display_weather(weather_data):
    if weather_data is None or 'weather' not in weather_data:
        print("Unable to fetch weather data.")
        return

    print("Current Weather:")
    print("Description:", weather_data['weather'][0]['description'])
    print("Temperature:", weather_data['main']['temp'], "°C")
    print("Humidity:", weather_data['main']['humidity'], "%")
    print("Wind Speed:", weather_data['wind']['speed'], "m/s")

def main():
    api_key = "YOUR_API_KEY"
    city = input("Enter a city name: ")

    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == '__main__':
main()

