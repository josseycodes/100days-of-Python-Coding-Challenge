import requests
import json

# API key from OpenWeatherMap
API_KEY = "YOUR_API_KEY"

def get_weather(city):
  """Gets the weather for a given city."""
  url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, API_KEY)
  response = requests.get(url)
  if response.status_code == 200:
    data = json.loads(response.content)
    return data
  else:
    return None

def main():
  city = input("Enter a city name: ")
  weather_data = get_weather(city)
  if weather_data is not None:
    print("Current weather conditions:")
    print("Temperature: {}°C".format(weather_data["main"]["temp"]))
    print("Humidity: {}%".format(weather_data["main"]["humidity"]))
    print("Weather description: {}".format(weather_data["weather"][0]["description"]))
    print()
    print("Forecast:")
    for forecast in weather_data["forecast"]:
      print("Date: {}".format(forecast["dt_txt"]))
      print("High: {}°C".format(forecast["high"]))
      print("Low: {}°C".format(forecast["low"]))
      print()
  else:
    print("No weather data found for {}".format(city))

if __name__ == "__main__":
  main()

