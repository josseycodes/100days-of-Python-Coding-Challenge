import feedparser

def read_rss_feed(url):
    """
    Fetches and parses the RSS feed from the given URL.
    """
    feed = feedparser.parse(url)
    return feed

def display_feed(feed):
    """
    Displays the titles and links of the entries in the RSS feed.
    """
    print("Feed Title:", feed.feed.title)
    print("Feed Description:", feed.feed.description)
    print("\nLatest Entries:")
    for entry in feed.entries:
        print("\nTitle:", entry.title)
        print("Link:", entry.link)

def main():
    # Example RSS feed URLs
    rss_feeds = [
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "http://feeds.bbci.co.uk/news/rss.xml",
        # Add more RSS feed URLs here
    ]

    # Read and display each RSS feed
    for url in rss_feeds:
        print("\nFetching RSS feed from:", url)
        feed = read_rss_feed(url)
        display_feed(feed)

if __name__ == "__main__":
    main()
