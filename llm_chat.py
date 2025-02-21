import os
import sys
from openai import OpenAI
import readline  # For better terminal input

# Load API key from environment or .env file
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "your-openai-api-key-here")
client = OpenAI()

def chat_with_llm():
    print("LLM Chat for Software Engineering (type 'exit' to quit)")
    print("Provide code or questions; include context for best results.")

    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break

        response = client.chat.completions.create(
            model="gpt-4o",  # Use your preferred model
            messages=[
                {"role": "system", "content": "You are a helpful software engineering assistant. Provide concise, actionable code suggestions."},
                {"role": "user", "content": user_input}
            ]
        )
        print("LLM:", response.choices[0].message.content)

if __name__ == "__main__":
    try:
        chat_with_llm()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
