Here's an example of a Python script that uses the BeautifulSoup library to scrape news headlines from a website. In this case, we'll scrape headlines from the BBC News website
This script starts by importing the necessary libraries: requests for sending HTTP requests and BeautifulSoup for parsing HTML.

We define the URL of the website we want to scrape, in this case, the BBC News website. We then use the requests library to send a GET request to that URL and retrieve the HTML content of the page.

Next, we create a BeautifulSoup object by passing in the HTML content and specifying the parser to use (html.parser).

We use the find_all() method on the BeautifulSoup object to find all the headlines on the page. In this example, we search for h3 elements with the class gs-c-promo-heading__title since that's the structure used on the BBC News website.

Finally, we iterate over the headlines and print each one.

You can modify this script to scrape different websites or extract different types of information by adjusting the HTML tags and class names used in the find_all() method.
