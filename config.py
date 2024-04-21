import os

# Load environment variables from .env file or the environment
from dotenv import load_dotenv
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# You could also add additional configuration settings here
# For example, the number of tweets to fetch, the language of tweets, etc.
TWEET_COUNT = 30
TWEET_LANGUAGE = "en"
