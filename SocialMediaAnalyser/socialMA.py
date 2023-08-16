import tweepy
from textblob import TextBlob

# Twitter API credentials (you need to get these from Twitter Developer platform)
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def analyze_tweets(keyword, count):
    tweets = api.search(q=keyword, lang='en', count=count)

    positive_tweets = 0
    negative_tweets = 0
    neutral_tweets = 0
    total_polarity = 0.0

    for tweet in tweets:
        print(f"Tweet: {tweet.text}")
        analysis = TextBlob(tweet.text)
        polarity = analysis.sentiment.polarity
        total_polarity += polarity

        if polarity > 0:
            positive_tweets += 1
        elif polarity < 0:
            negative_tweets += 1
        else:
            neutral_tweets += 1

    print(f"\nPositive Tweets: {positive_tweets}")
    print(f"Negative Tweets: {negative_tweets}")
    print(f"Neutral Tweets: {neutral_tweets}")

    avg_polarity = total_polarity / count
    print(f"\nAverage Sentiment Polarity: {avg_polarity:.2f}")

if __name__ == "__main__":
    keyword_to_search = input("Enter a keyword to search on Twitter: ")
    number_of_tweets = int(input("Enter the number of tweets to analyze: "))

    analyze_tweets(keyword_to_search, number_of_tweets)

