import matplotlib.pyplot as plt
from analyze_sentiments import analyze_tweets
from fetch_tweets import fetch_tweets, authenticate_twitter_api

def plot_sentiment_distribution(sentiments):
    """
    Plots a bar chart of the sentiment distribution.
    
    Parameters:
    sentiments (list): A list of sentiment results from the sentiment analysis.
    """
    # Count the occurrences of each sentiment
    sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
    for sentiment in sentiments:
        sentiment_counts[sentiment['label'].lower()] += 1

    # Prepare the bar chart
    labels = sentiment_counts.keys()
    values = sentiment_counts.values()
    
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['green', 'red', 'blue'])
    plt.xlabel('Sentiments')
    plt.ylabel('Number of Tweets')
    plt.title('Distribution of Sentiments in Tweets')
    plt.show()

def main():
    """
    Main function to fetch tweets, analyze them, and plot the results.
    """
    # Authenticate and fetch tweets
    api = authenticate_twitter_api()
    query = "#examplehashtag"  # Change to your desired query
    tweets = fetch_tweets(api, query)

    # Analyze the sentiments of fetched tweets
    if tweets:
        sentiments = analyze_tweets(tweets)
        plot_sentiment_distribution(sentiments)

if __name__ == "__main__":
    main()
