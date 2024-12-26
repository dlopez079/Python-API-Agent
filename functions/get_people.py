import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_people():
    """
    Fetches a list of people from the Follow Up Boss API.

    Returns:
        list: A list of people in JSON format if the request is successful.
        None: If there's an error during the request or if environment variables are missing.
    """
    api_key = os.getenv('FOLLOW_UP_BOSS_API_KEY')
    base_url = os.getenv('FOLLOW_UP_BOSS_URL')

    if not api_key or not base_url:
        print("Error: FOLLOW_UP_BOSS_API_KEY or FOLLOW_UP_BOSS_URL is not set in the environment variables.")
        return None

    url = f'{base_url}/people'

    try:
        response = requests.get(url, auth=HTTPBasicAuth(api_key, ''))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
