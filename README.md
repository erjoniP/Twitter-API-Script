# Twitter-API-Script

This Python script demonstrates how to authenticate with the Twitter API using OAuth 1.0a and perform a "like" action on a tweet using the `POST /2/users/:id/likes` endpoint. The script includes error handling for API rate limits and authentication errors.

## Features

- **OAuth 1.0a Authentication:** Uses `requests-oauthlib` to handle OAuth 1.0a.
- **Like a Tweet:** Sends a POST request to like a tweet based on its ID.
- **Error Handling:** Checks for rate limits (HTTP 429) and authentication issues (HTTP 401/403).
- **Logging:** Provides informative log messages to track script execution.

## Prerequisites

- Python 3.x installed on your machine.
- A Twitter Developer account with a created app.
- Twitter API credentials with **Read and Write** permissions.

## Installation

1. **Clone the repository** (if applicable) or download the files.

2. **Install required Python packages.** You can install the dependencies using `pip`. It is recommended to use a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install python-dotenv requests-oauthlib

3. **Create a .env file in the same directory as twitter_script.py and add your API credentials. For example:
   ```
   TWITTER_API_KEY=FAKE_API_KEY_123456
   TWITTER_API_SECRET_KEY=FAKE_API_SECRET_ABCDEF
   TWITTER_ACCESS_TOKEN=FAKE_ACCESS_TOKEN_1234567890
   TWITTER_ACCESS_TOKEN_SECRET=FAKE_ACCESS_TOKEN_SECRET_ABCDEF
   TWITTER_USER_ID=1234567890
Note: The values above are sample (fake) credentials. Replace them with your actual credentials from the Twitter Developer Portal. Ensure your app has Read and Write permissions, and if you change permissions, regenerate your access token and secret.

## How to Run the Script

1. Activate your virtual environment (if not already activated).

2. Run the script:
   ```
   python twitter_script.py
The script will attempt to "like" the tweet with the ID specified in the code (hard-coded for demonstration purposes). You can modify twitter_script.py to accept dynamic input if needed.
