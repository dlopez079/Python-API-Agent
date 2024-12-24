import requests
import base64
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("FOLLOW_UP_BOSS_API_KEY")
BASE_URL = "https://api.followupboss.com/v1"

# Create the Basic Auth header
auth_header = base64.b64encode(f"{API_KEY}:".encode("utf-8")).decode("utf-8")

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/json",
}

# Enhanced error handling function
def get_people():
    try:
        response = requests.get(f"{BASE_URL}/people", headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Print HTTP-specific error
        print(f"Response content: {response.text}")  # Include response content
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Print general request errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Catch other errors
    return None

# Function to interact with OpenAI
def ask_chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace with "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Return the assistant's response
        return response['choices'][0]['message']['content'].strip()
    except openai.BadRequestError as e:
        print(f"Invalid request: {e}")
    except openai.AuthenticationError as e:
        print(f"Authentication failed: {e}")
    except openai.APIConnectionError as e:
        print(f"Failed to connect to OpenAI API: {e}")
    except openai.RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def generate_follow_up_suggestions():
    people = get_people()
    if not people:
        print("No data fetched from Follow Up Boss.")
        return
    
    # Create a prompt for ChatGPT
    prompt = "Provide follow-up suggestions for these leads:\n\n"
    for person in people.get("people", []):
        name = person.get("name", "Unknown")
        last_contact = person.get("lastContacted", "Never")
        prompt += f"- Name: {name}, Last Contacted: {last_contact}\n"

    # Use ChatGPT to generate suggestions
    suggestions = ask_chatgpt(prompt)
    print("\nAI Follow-Up Suggestions:\n")
    print(suggestions)


# Example usage
if __name__ == "__main__":
    generate_follow_up_suggestions()
