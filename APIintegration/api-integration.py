import requests

# Replace 'YOUR_API_KEY' with the actual API key you obtained from OpenWeatherMap
API_KEY = 'YOUR_API_KEY'
CITY_NAME = 'New York'  # Replace with the desired city name

# URL for the API request
url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}'

# Make the API request
response = requests.get(url)
data = response.json()

# Extract relevant weather data
weather = data['weather'][0]['main']
temperature = data['main']['temp']
humidity = data['main']['humidity']

# Display the retrieved data
print(f"Weather in {CITY_NAME}: {weather}")
print(f"Temperature: {temperature} K")
print(f"Humidity: {humidity}%")

