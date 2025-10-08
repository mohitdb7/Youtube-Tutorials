from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

groq_key = os.environ.get("GROQ_API_KEY")

groq_client = Groq(api_key=groq_key)

chat_result = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role":"system",
            "content":("My name is Mohit, always address me with my name where you are responding to any of my queries." 
                       "Explain me briefly. Do not add too much of details")
        },
        {
            "role": "user",
            "content":"Explain me Transformers in generative AI"
        }
    ]
)

print(chat_result.choices[0].message.content)
