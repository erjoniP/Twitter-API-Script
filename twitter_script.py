import os
import logging
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session

# Load API credentials from the .env file
load_dotenv()

# Setup logging to display status messages
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Retrieve Twitter API credentials from environment variables
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_USER_ID = os.getenv("TWITTER_USER_ID")  # The user ID who is liking tweets

def like_tweet(tweet_id):
    """
    Likes a tweet specified by tweet_id using Twitter API v2 endpoint.
    
    Endpoint: POST /2/users/:id/likes
    :parameter tweet_id: The ID of the tweet to like.
    """
    # Construct the endpoint URL using the authenticated user's ID
    url = f"https://api.twitter.com/2/users/{TWITTER_USER_ID}/likes"
    payload = {"tweet_id": tweet_id}
    # Create an OAuth1Session for authenticating the request using OAuth 1.0a
    oauth = OAuth1Session(API_KEY,
                          client_secret=API_SECRET_KEY,
                          resource_owner_key=ACCESS_TOKEN,
                          resource_owner_secret=ACCESS_TOKEN_SECRET)
    try:
        response = oauth.post(url, json=payload)
        if response.status_code == 200:
            logger.info("Tweet liked successfully.")
        elif response.status_code == 429:
            logger.error("Rate limit exceeded. Please wait and try again later.")
        elif response.status_code in [401, 403]:
            logger.error("Authentication error. Check your API credentials.")
        else:
            logger.error(f"Failed to like tweet. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

def main():
    # tweet ID to like
    tweet_id = "1894913640748179538"
    
    # Ensures all required credentials are available
    if not all([API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, TWITTER_USER_ID]):
        logger.error("One or more Twitter API credentials are missing. Please check your .env file.")
        return
    
    like_tweet(tweet_id)

if __name__ == "__main__":
    main()
