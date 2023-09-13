import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon if you haven't already
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    # Analyze sentiment using VADER
    sentiment_scores = analyzer.polarity_scores(text)
    
    # Determine sentiment label
    if sentiment_scores['compound'] >= 0.05:
        return "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    # Input social media post or comment
    social_media_text = input("Enter the social media post or comment: ")
    
    # Analyze sentiment
    sentiment = analyze_sentiment(social_media_text)
    
    # Display the result
    print(f"Sentiment: {sentiment}")

