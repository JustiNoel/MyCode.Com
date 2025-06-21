import requests
import json
import os

# Securely store your API key (do NOT hardcode it)
# Option 1: Set it as an environment variable before running the script
# On Windows CMD: set XAI_API_KEY=xai-nBvITVkxAf9a3XjAUZGbftpczJg3821HMF2csM6yzPFVfQMjXvGQ7NccIMYz7Lp3qtWm3S6MS8H4hiil
# On Unix/Linux/Mac: export XAI_API_KEY=xai-nBvITVkxAf9a3XjAUZGbftpczJg3821HMF2csM6yzPFVfQMjXvGQ7NccIMYz7Lp3qtWm3S6MS8H4hiil
API_KEY = os.getenv("XAI_API_KEY")  # Reads the key from environment variable
if not API_KEY:
    print("Error: XAI_API_KEY environment variable not set.")
    exit(1)

API_URL = "https://api.x.ai/v1/chat/completions"  # Grok's chat completion endpoint
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("Chat with Grok! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    # Prepare the payload for the API request
    payload = {
        "model": "grok-beta",  # Use Grok model (e.g., grok-beta, grok-3-beta, etc.)
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,  # Controls response randomness (adjust as needed)
        "max_tokens": 1000   # Limits response length (adjust as needed)
    }

    try:
        # Send request to xAI API
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the response
        response_data = response.json()
        grok_response = response_data["choices"][0]["message"]["content"]

        print("Grok:", grok_response)
    except requests.exceptions.RequestException as e:
        print("Error:", e)