import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def generate_script(topic):
    prompt = (
        "You are a professional YouTube scriptwriter. "
        "Create a compelling, engaging, and informative script on the topic: '{}'.\n"
        "Structure:\n"
        "- Hook\n"
        "- Intro\n"
        "- Main Content (Bullet Points or Segments)\n"
        "- Outro with CTA\n"
        "Keep it conversational and creative."
    ).format(topic)

    data = {
        "model": "llama3-70b-8192",  # Groq's fast model
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"