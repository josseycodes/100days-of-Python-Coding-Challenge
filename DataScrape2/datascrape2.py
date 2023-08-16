import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# URL to scrape weather data from
url = "https://www.examplewebsite.com/weather"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract temperature data (replace with actual HTML tags and classes)
temperature_data = soup.find_all("span", class_="temperature")

# Lists to store data for visualization
dates = []
temperatures = []

# Iterate through the temperature data and extract relevant information
for data in temperature_data:
    date = data.get_text()
    temperature = float(data["data-temperature"])

    dates.append(date)
    temperatures.append(temperature)

# Data visualization using Matplotlib
plt.figure(figsize=(10, 6))
plt.bar(dates, temperatures, color="blue")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trends")
plt.xticks(rotation=45)
plt.tight_layout()

# Display the bar chart
plt.show()

