import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize NLTK tools
lemmatizer = WordNetLemmatizer()
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

# Load the pretrained conversational model (DialoGPT)
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Define sustainability-focused responses
sustainability_responses = {
    "energy": "Try using LED bulbs, turning off unused appliances, or insulating your home to save energy!",
    "meal": "Consider a plant-based meal like a lentil soup or a veggie stir-fry to reduce your carbon footprint.",
    "transport": "Opt for biking, walking, or public transport instead of driving to lower emissions.",
    "water": "Save water by taking shorter showers and fixing leaks promptly!",
    "waste": "Reduce waste by composting food scraps and using reusable bags!",
    "greeting": "Hi! I’m your Sustainability Coach. How can I help you live more sustainably today?",
    "default_sustainability": "I’m not sure about that, but a good start is reducing energy use, eating plant-based, and minimizing waste!"
}

# Store user data
user_data = {
    "energy_usage_kwh": None,
    "points": 0
}

# Function to analyze energy usage and give a tip
def analyze_energy_usage(energy_usage):
    if energy_usage is None:
        return "Please tell me your monthly energy usage in kWh (e.g., 'My energy usage is 500 kWh')."
    elif energy_usage > 1000:
        tip = "Your usage is very high! Consider a home energy audit."
    elif energy_usage > 400:
        tip = "Your energy usage is high! Try using LED bulbs or turning off unused appliances."
    elif energy_usage > 200:
        tip = "Your energy usage is moderate. Consider using a programmable thermostat."
    else:
        tip = "Great job! Your energy usage is low. Keep it up!"
    
    points_message = award_points(energy_usage)
    return f"{tip} {points_message} Total points: {user_data['points']}"

# Function to extract energy usage from user input
def extract_energy_usage(user_input):
    tokens = word_tokenize(user_input.lower())
    for i, token in enumerate(tokens):
        if token == "kwh" and i > 0:
            try:
                usage = float(tokens[i-1])
                user_data["energy_usage_kwh"] = usage
                return True
            except ValueError:
                pass
    return False

# Function to award points
def award_points(energy_usage):
    if energy_usage <= 200:
        user_data["points"] += 20
        return "Great job! You earned 20 points for low energy usage."
    elif energy_usage <= 400:
        user_data["points"] += 10
        return "Good effort! You earned 10 points for moderate energy usage."
    else:
        return "Keep working on reducing your energy usage to earn points!"

# Function to generate a response using DialoGPT
def generate_dialogpt_response(user_input, chat_history_ids=None):
    # Encode the user input
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    
    # Append the new user input to the chat history
    bot_input_ids = new_user_input_ids if chat_history_ids is None else torch.cat([chat_history_ids, new_user_input_ids], dim=1)
    
    # Generate a response
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    
    # Decode the response
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response, chat_history_ids

# Function to process user input and return a response
def get_response(user_input, chat_history_ids=None):
    # Check if user is providing energy usage
    if extract_energy_usage(user_input):
        return analyze_energy_usage(user_data["energy_usage_kwh"]), chat_history_ids
    
    # Tokenize and lemmatize the input
    tokens = word_tokenize(user_input.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Check for specific queries
    if any(word in tokens for word in ["points", "score"]):
        return f"Your total points are: {user_data['points']}", chat_history_ids
    elif any(word in tokens for word in ["hi", "hello", "hey", "greetings"]):
        return sustainability_responses["greeting"], chat_history_ids
    elif any(word in tokens for word in ["energy", "electricity", "power"]):
        return sustainability_responses["energy"], chat_history_ids
    elif any(word in tokens for word in ["meal", "food", "eat"]):
        return sustainability_responses["meal"], chat_history_ids
    elif any(word in tokens for word in ["transport", "travel", "commute"]):
        return sustainability_responses["transport"], chat_history_ids
    elif any(word in tokens for word in ["water", "shower"]):
        return sustainability_responses["water"], chat_history_ids
    elif any(word in tokens for word in ["waste", "trash", "recycle"]):
        return sustainability_responses["waste"], chat_history_ids
    else:
        # Check if the input is sustainability-related
        sustainability_keywords = ["sustainab", "environment", "green", "eco", "carbon", "climate"]
        if any(keyword in user_input.lower() for keyword in sustainability_keywords):
            return sustainability_responses["default_sustainability"], chat_history_ids
        
        # Fall back to DialoGPT for unrelated queries
        response, new_chat_history_ids = generate_dialogpt_response(user_input, chat_history_ids)
        return response, new_chat_history_ids

# Main chat loop
def chat():
    print("Welcome to your Sustainability Coach! Type 'exit' to stop.")
    chat_history_ids = None
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! Stay sustainable!")
            break
        response, chat_history_ids = get_response(user_input, chat_history_ids)
        print("AI: " + response)

# Run the chatbot
if __name__ == "__main__":
    chat()