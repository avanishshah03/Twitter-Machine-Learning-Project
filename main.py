from fetch_tweets import fetch_tweets, authenticate_twitter_api
from analyze_sentiments import analyze_tweets
from visualize_results import plot_sentiment_distribution

def main():
    """
    Main execution function that fetches tweets, analyzes their sentiments,
    and plots the sentiment distribution.
    """
    # Step 1: Authenticate Twitter API
    api = authenticate_twitter_api()

    # Step 2: Define your query
    query = "#examplehashtag"  # Replace with your desired query

    # Step 3: Fetch tweets
    print("Fetching tweets...")
    tweets = fetch_tweets(api, query)
    if not tweets:
        print("No tweets found for the given query.")
        return

    # Step 4: Analyze sentiments
    print("Analyzing sentiments...")
    sentiments = analyze_tweets(tweets)
    
    # Step 5: Visualize results
    print("Visualizing results...")
    plot_sentiment_distribution(sentiments)

if __name__ == "__main__":
    main()
