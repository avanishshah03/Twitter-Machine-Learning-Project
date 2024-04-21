import tweepy
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, TWEET_COUNT, TWEET_LANGUAGE

def authenticate_twitter_api():
    """
    Function to handle Twitter API authentication.
    """
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def fetch_tweets(api, query):
    """
    Fetches tweets based on a search query and returns a list of tweets.
    """
    tweets = []
    try:
        # Call the user_timeline function from Tweepy
        for tweet in tweepy.Cursor(api.search_tweets,
                                   q=query,
                                   lang=TWEET_LANGUAGE,
                                   tweet_mode='extended').items(TWEET_COUNT):
            tweets.append(tweet.full_text)
    except tweepy.TweepyException as e:
        print("An error occurred while fetching tweets:", str(e))
    return tweets

def main():
    """
    Main function to authenticate and fetch tweets.
    """
    api = authenticate_twitter_api()
    query = "#examplehashtag"  # Example hashtag, change to your targeted search
    tweets = fetch_tweets(api, query)
    print("Fetched {} tweets".format(len(tweets)))
    for tweet in tweets[:10]:  # Print first 10 tweets to check
        print(tweet)

if __name__ == "__main__":
    main()
