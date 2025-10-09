import os

# from gtts import gTTS

# # Text you want to convert to speech
# text = "Hello! This is a simple text to speech conversion example."

# # Language (English)
# language = 'en'

# # Create gTTS object
# tts = gTTS(text=text, lang=language, slow=False)

# # Save the audio file
# tts.save("output.mp3")

# # Play the audio file (works on Windows)
# # os.system("start output.mp3")
# # On MacOS, use:
# os.system("afplay output.mp3")


import pyttsx3


def reply_with_audio(response: str):
    engine = pyttsx3.init()
    completed = False
    try:
        # Set speech rate (default is about 200 words per minute)
        engine.setProperty('rate', 210)  # Increase the rate for faster speech

        engine.say(response if response and (response != "") else "I did not receive any response")
        engine.runAndWait()
        return True
    except Exception as e:
        print(f"Exception in Text to Speech {str(e)}")