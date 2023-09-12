import tweepy
from textblob import TextBlob

# Define your Twitter API credentials (if you're analyzing Twitter data)
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API (if you're analyzing Twitter data)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to perform sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    
    # Determine sentiment polarity (-1 to 1, where -1 is negative, 0 is neutral, and 1 is positive)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Example social media post or comment
social_media_post = "I love the new Crownex Reed Diffuser. The scent is amazing!"

# Analyze sentiment
sentiment = analyze_sentiment(social_media_post)
print(f"Sentiment: {sentiment}")

