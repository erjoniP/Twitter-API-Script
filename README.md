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
