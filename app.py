from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("AI Chatbot started!")
print("Type 'exit' to quit.\n")

previous_interaction_id = None

while True:

    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Bot: Goodbye!")
        break

    if previous_interaction_id is None:

        response = client.interactions.create(
            model="gemini-3.8-flash",
            input=user_message
        )

    else:

        response = client.interactions.create(
            model="gemini-3.8-flash",
            input=user_message,
            previous_interaction_id=previous_interaction_id
        )

    print("Bot:", response.output_text)

    previous_interaction_id = response.id