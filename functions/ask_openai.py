from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

def ask_openai():
    
    # Access the environment variables
    api_key = os.getenv("OPENAI_API_KEY")

    # If there is no key, the we will return a message indicating the issue.
    if not api_key:
        print("Error: OPENAI_API_KEY is not set in the environment variables.")
        return None

    client = OpenAI()

    prompt = f"You're a sales assistant. Write a personalized follow-up email"
    userInput = f"Are semicolons optional in javascript"

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "developer", 
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": userInput
                    }
                ]
            }
            
        ]
    )

    print(completion.choices[0].message.content)

# Example usage
if __name__ == "__main__":
    ask_openai()
