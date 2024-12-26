from functions.generate_follow_up_message import generate_follow_up_message
from functions.get_people import get_people
from functions.ask_openai import ask_openai
import json

def main():
    # Fetch contacts from Follow Up Boss
    response_data = get_people()
    if not response_data:
        print("No contacts retrieved.")
        return

    # Extract the list of people from the response
    contacts = response_data.get('people', [])
    if not contacts:
        print("No contacts found in the response.")
        return

    # Pretty-print the entire contacts data for inspection
    #print("Contacts Data:")
    #print(json.dumps(contacts, indent=4))

    # Iterate over each contact and print specific user information
    for contact in contacts:
        first_name = contact.get('firstName', 'N/A')
        last_name = contact.get('lastName', 'N/A')
        emails = contact.get('emails', [])
        
        if emails:
            for email in emails:
                email_address = email.get('value', 'N/A')
                #email_type = email.get('type', 'N/A')
                # print(f"  Email ({email_type}): {email_address}")
        else:
            print("  No email addresses found.")

        print(f"Name: {first_name} {last_name}, Email: {email_address}")

        # Generate follow-up message using OpenAI
        follow_up_message = generate_follow_up_message(first_name, last_name)
        print(f"Follow-up message for {first_name} {last_name}:\n{follow_up_message}\n")

if __name__ == "__main__":
    main()
