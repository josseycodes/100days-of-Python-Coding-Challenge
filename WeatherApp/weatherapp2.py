# Import requests module to make api calls
import requests

# Define the base url for the openweathermap api
base_url = "http://api.openweathermap.org/data/2.5/"

# Define the api key (replace with your own)
api_key = "your_api_key_here"

# Define the units for temperature (metric or imperial)
units = "metric"

# Ask the user for the location
location = input("Enter the city name: ")

# Build the url for the current weather data
current_url = base_url + "weather?q=" + location + "&appid=" + api_key + "&units=" + units

# Make a get request and store the response
current_response = requests.get(current_url)

# Check if the request was successful
if current_response.status_code == 200:
    # Convert the response to a json object
    current_data = current_response.json()

    # Extract the relevant information
    current_temp = current_data["main"]["temp"]
    current_feels_like = current_data["main"]["feels_like"]
    current_humidity = current_data["main"]["humidity"]
    current_pressure = current_data["main"]["pressure"]
    current_weather = current_data["weather"][0]["description"]

    # Print the current weather conditions
    print(f"Current weather in {location}:")
    print(f"Temperature: {current_temp} °C")
    print(f"Feels like: {current_feels_like} °C")
    print(f"Humidity: {current_humidity} %")
    print(f"Pressure: {current_pressure} hPa")
    print(f"Weather: {current_weather}")

else:
    # Print an error message
    print("Sorry, something went wrong. Please try again.")

# Build the url for the forecast data
forecast_url = base_url + "forecast?q=" + location + "&appid=" + api_key + "&units=" + units

# Make a get request and store the response
forecast_response = requests.get(forecast_url)

# Check if the request was successful
if forecast_response.status_code == 200:
    # Convert the response to a json object
    forecast_data = forecast_response.json()

    # Extract the list of forecasts
    forecast_list = forecast_data["list"]

    # Print the forecast for the next 5 days
    print(f"Forecast for {location}:")

    # Loop through the list of forecasts
    for forecast in forecast_list:
        # Extract the date and time
        date_time = forecast["dt_txt"]

        # Extract the temperature and weather
        temp = forecast["main"]["temp"]
        weather = forecast["weather"][0]["description"]

        # Print the date, time, temperature and weather
        print(f"{date_time}: {temp} °C, {weather}")

else:
    # Print an error message
    print("Sorry, something went wrong. Please try again.")

