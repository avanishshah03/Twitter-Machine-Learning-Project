from transformers import pipeline
from fetch_tweets import fetch_tweets, authenticate_twitter_api

def load_sentiment_analyzer():
    """
    Load the sentiment analysis model using Hugging Face's pipeline.
    """
    return pipeline("sentiment-analysis")

def analyze_tweets(tweets):
    """
    Analyze the sentiment of each tweet in the list of tweets.
    
    Parameters:
    tweets (list): List of tweet texts.
    
    Returns:
    list: List of dictionaries with each tweet's text and its sentiment score.
    """
    sentiment_analyzer = load_sentiment_analyzer()
    results = sentiment_analyzer(tweets)
    return results

def main():
    """
    Main function to fetch tweets, analyze them, and print the results.
    """
    # Authenticate and fetch tweets
    api = authenticate_twitter_api()
    query = "#examplehashtag"  # Change to your desired query
    tweets = fetch_tweets(api, query)

    # Analyze the sentiments of fetched tweets
    if tweets:
        analyzed_tweets = analyze_tweets(tweets)
        for tweet, sentiment in zip(tweets, analyzed_tweets):
            print(f"Tweet: {tweet}\nSentiment: {sentiment}\n")

if __name__ == "__main__":
    main()
