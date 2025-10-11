# 🗣️ EchoMind: Talk to Your AI. 
Voice Assistant with Whisper, VAD, and Groq

This project is a simple voice-interaction system built in Python that allows users to speak into their microphone, automatically detects speech using WebRTC's Voice Activity Detection (VAD), transcribes it using OpenAI's Whisper model, and sends the transcribed text to a large language model (LLM) hosted via **Groq**. The response is then read out loud using text-to-speech (TTS).

---

## 🎯 Features

* 🎤 **Voice Activity Detection (VAD)** using `webrtcvad` to auto-start and auto-stop recording.
* 🧠 **Speech-to-Text** using `openai/whisper`.
* 💬 **LLM Interaction** via **Groq API**.
* 🔊 **Text-to-Speech (TTS)** using `pyttsx3`.
* 🧪 **Rich CLI Output** for debugging and interactive use.

---

## 📁 Project Structure

```
.
├── agent_interaction.py     # Main entrypoint - connects all components
├── speech_to_text.py        # Handles voice recording and Whisper transcription
├── text_to_speech.py        # Handles converting response text to speech
├── recordings/              # Folder where .wav recordings are saved
├── .env                     # Environment file to store API key
```

---

## 🧪 Demo Flow

1. Run `agent_interaction.py`
2. Speak when prompted.
3. The system detects speech and records until you stop speaking.
4. Your voice is transcribed using Whisper.
5. The transcription is sent to Groq’s LLM.
6. The LLM’s response is printed and spoken aloud using text-to-speech.

---

## 🛠️ Requirements

Install dependencies using `pip`:

```bash
pip install webrtcvad pyaudio openai-whisper pyttsx3 python-dotenv groq rich numpy ffmpeg
```

```
uv sync --active
```

> **Note:** `pyaudio` may require system-level dependencies. For macOS/Linux, install `portaudio` first. For Windows, use precompiled wheels if needed.

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🚀 Running the App

Make sure your microphone is set up and then run:

```bash
uv run  speech_to_speech/agent/agent_interaction.py
```

---

## 📦 Dependencies Overview

| Package     | Purpose                            |
| ----------- | ---------------------------------- |
| `pyaudio`   | Microphone input and WAV recording |
| `webrtcvad` | Detecting speech and silence       |
| `whisper`   | Transcribing audio to text         |
| `groq`      | Accessing Groq's LLM via API       |
| `pyttsx3`   | Text-to-speech output              |
| `rich`      | Pretty CLI printing for output     |
| `dotenv`    | Loading environment variables      |

---

## 📂 Output

* WAV files are stored in the `recordings/` directory with timestamped filenames.
* The terminal will show:

  * VAD status (when speech starts/stops)
  * Transcribed text
  * Model response (rendered in markdown or JSON)
* The LLM response is spoken aloud via your speakers.

---

## 💡 Example Use Cases

* Quick voice-based Q&A system.
* Accessibility interface for interacting with LLMs.
* Prototype for voice-enabled AI agents.

---

## 📌 Notes

* The Whisper model used is `"base"` — upgrade to `"small"`, `"medium"`, or `"large"` for better accuracy.
* Only English is supported (`language="en"` hardcoded).
* Assumes single-channel (mono) 16kHz audio input.
* Ensure the `recordings/` folder exists or the script may fail.

---

## 🧹 To-Do / Improvements

* Add GUI or web interface
* Add multi-language support
* Handle longer conversations (chat history)
* Stream transcription instead of saving WAV
* Use Groq’s vision or multimodal features

---

## 🧾 License

MIT License

---

#### Installation
- brew install ffmpeg
- uv venv .venv
- source .venv/bin/activate   
- uv add SpeechRecognition pyaudio 
- Use `Command + Shift + P` to select the python interpreter

---
Made with ❤️ By `Mohit Kumar Dubey`
---
