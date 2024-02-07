import tweepy
from textblob import TextBlob

class SocialMediaAnalyzer:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        # Authenticate with Twitter API
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def analyze_sentiment(self, query, count=100):
        # Get tweets
        tweets = self.api.search(q=query, count=count)

        # Analyze sentiment
        positive_count = 0
        negative_count = 0
        neutral_count = 0

        for tweet in tweets:
            analysis = TextBlob(tweet.text)
            if analysis.sentiment.polarity > 0:
                positive_count += 1
            elif analysis.sentiment.polarity < 0:
                negative_count += 1
            else:
                neutral_count += 1
        
        total_tweets = positive_count + negative_count + neutral_count

        # Calculate percentages
        positive_percentage = (positive_count / total_tweets) * 100
        negative_percentage = (negative_count / total_tweets) * 100
        neutral_percentage = (neutral_count / total_tweets) * 100

        print("Sentiment Analysis:")
        print("-------------------")
        print("Positive tweets:", positive_percentage, "%")
        print("Negative tweets:", negative_percentage, "%")
        print("Neutral tweets:", neutral_percentage, "%")

    def get_trending_topics(self, location):
        trends = self.api.trends_place(location)

        print("Trending Topics in", location)
        print("---------------------------")
        for trend in trends[0]['trends']:
            print(trend['name'])

# Example usage:
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

analyzer = SocialMediaAnalyzer(consumer_key, consumer_secret, access_token, access_token_secret)

# Analyze sentiment for a query
analyzer.analyze_sentiment(query='Python')

# Get trending topics for a location (WOEID: 1 for Worldwide)
analyzer.get_trending_topics(location=1)
