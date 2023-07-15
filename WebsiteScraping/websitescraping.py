import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.bbc.com/news"

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Find all news headlines on the page
headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")

# Print the headlines
for headline in headlines:
    print(headline.text.strip())

