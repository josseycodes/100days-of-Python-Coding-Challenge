import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract specific information from the page
        # Example: Extracting all the links on the page
        links = soup.find_all('a')
        
        # Print the extracted information
        for link in links:
            print(link.get('href'))
        
        # Alternatively, you can save the extracted information to a structured format
        # Example: Saving links to a text file
        with open('links.txt', 'w') as file:
            for link in links:
                file.write(link.get('href') + '\n')
                
        print("Data scraped successfully and saved to 'links.txt'.")
    else:
        print("Failed to scrape data. Status code:", response.status_code)

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    scrape_url(url)
