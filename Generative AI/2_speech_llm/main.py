# #%% Import Libraries
# import speech_recognition as sr

# #%% Run Main
# def main():
#     print("Hello from speech-to-text!")
#     print(sr.__version__)

#     for index, name in enumerate(sr.Microphone.list_microphone_names()):
#         print(index, name)
    
#     speech_to_text()

# def speech_to_text():
#     rec = sr.Recognizer()

#     with sr.Microphone(device_index=0) as source:
#         print("start Talking...")
#         audio = rec.listen(source=source)

#         try:
#             text = rec.recognize_google(audio, language="en-EN")
#             print(f"You said {text}")
#         except Exception as e:
#             print(f"Exception is {str(e)}")


# if __name__ == "__main__":
#     main()
