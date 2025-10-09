import os
from dotenv import load_dotenv
from speech_to_text import record_speech_and_convert_to_text
from text_to_speech import reply_with_audio
from groq import Groq

load_dotenv()

groq_key = os.environ.get("GROQ_API_KEY")
print(f"{groq_key[:5]}...{groq_key[:-5]}")

client = Groq(
    api_key=groq_key,
)

def print_llm_response(response: str):
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.json import JSON

    console = Console()
    try:
        console.print(JSON(response))
    except Exception:
        console.print(Markdown(response))

def groq_interact():

    while True:
        print("Starting to record")
        user_query = record_speech_and_convert_to_text()

        print(f"User query is {user_query}")
        query_content_blocks = [{"type": "text", "text": f"User question: {user_query}"}]


        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful and factual AI assistant that can reason over english text. Your name is Friday."
                    "My name is Mohit. Always address me with my name"
                    "Your task is to answer the user's question"
                    "Explain in brief, do not make it very long. Keep it crisp and informative"
                    "If you do not know something, then answer that you don't know"
                    "If user shows interest to Exit the conversation the return just 'Exit' in the response"
                    "Do not give option for a followup question. You do not have memory."
                )
            },
            {
                "role": "user",
                "content": query_content_blocks
            }
        ]

        print("Model is generating the response")
        # --- Step 7: Send multimodal input to Groq ---
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        response_text = chat_completion.choices[0].message.content
        print("Model is about to reply...")
        print_llm_response(response_text)

        if response_text.lower() == "exit":
            break

        result = reply_with_audio(response=response_text)

        if result:
            print("LLM finished responding, It will again ask you to speak")
        
        print("\n\n", "*"*50)


groq_interact()
