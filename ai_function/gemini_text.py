from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def generate_text(prompt):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text


prompt = "What is the capital of France?"
agent = generate_text(prompt)
print(agent)
