import google.generativeai as genai

API_KEY ="AIzaSyCxueBO1kp_REi5WFgt1FsbBay4QTskErM"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0_flash")
chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)