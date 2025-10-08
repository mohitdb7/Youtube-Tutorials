from groq import Groq
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.json import JSON

load_dotenv()

groq_key = os.environ.get("GROQ_API_KEY")

groq_client = Groq(api_key=groq_key)

chat_result = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role":"system",
            "content":("My name is Mohit, always address me with my name where you are responding to any of my queries.")
        },
        {
            "role": "user",
            "content":"Explain me Transformers in generative AI"
        }
    ]
)

def print_llm_response(response: str):
    console = Console()
    try:
        console.print(JSON(response))
    except Exception:
        console.print(Markdown(response))

print_llm_response(chat_result.choices[0].message.content)
