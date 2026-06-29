from groq import Groq
from dotenv import load_dotenv
import os 

load_dotenv()


API_KEY = os.getenv("API_KEY")
client = Groq(api_key=API_KEY)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Parle comme un chat."
        },
        {
            "role": "user",
            "content": "ecris une chonson "
        }
    ],
    model="llama-3.3-70b-versatile"
)

print(chat_completion.choices[0].message.content)