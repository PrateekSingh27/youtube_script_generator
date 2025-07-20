import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def generate_script(topic):
    system_prompt = (
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
        "model": "openrouter/openchat/openchat-3.5-1210",  # Free model
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": system_prompt}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"