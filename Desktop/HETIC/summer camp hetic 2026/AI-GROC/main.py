from groq import Groq
from dotenv import load_dotenv
import os 

load_dotenv()

with open("context.txt", "r", encoding="utf-8") as f:
    context = f.read()

with open("remarques.txt", "r") as f:
    remarques = f.read()



API_KEY = os.getenv("API_KEY")
client = Groq(api_key=API_KEY)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": context , 
        },
        {
            "role": "user",
            "content": remarques ,
        }
    ],
    model="llama-3.3-70b-versatile"
)

print(chat_completion.choices[0].message.content)