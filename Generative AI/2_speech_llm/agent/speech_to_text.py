import collections
import sys
import signal
import webrtcvad
import pyaudio
import wave
import whisper
import numpy as np
import tempfile
from datetime import datetime
import os


# Audio config
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000  # Whisper prefers 16kHz
FRAME_DURATION_MS = 30
FRAME_SIZE = int(RATE * FRAME_DURATION_MS / 1000)
CHUNK_DURATION_MS = 30  # ms
CHUNK_SIZE = int(RATE * CHUNK_DURATION_MS / 1000)
SILENCE_TIMEOUT = 1  # seconds

vad = webrtcvad.Vad(2)  # Aggressiveness mode: 0 (least) to 3 (most aggressive)

def record_voice_until_silence():
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK_SIZE)

    print("🎤 Waiting for speech... (Speak into the mic)")

    frames = []
    silence_counter = 0
    speaking = False

    try:
        while True:
            data = stream.read(CHUNK_SIZE, exception_on_overflow=False)

            is_speech = vad.is_speech(data, RATE)

            if is_speech:
                if not speaking:
                    print("🗣️ Speech detected, recording...")
                    speaking = True
                frames.append(data)
                silence_counter = 0
            else:
                if speaking:
                    silence_counter += 1
                    if silence_counter > int(SILENCE_TIMEOUT * 1000 / CHUNK_DURATION_MS):
                        print("🔇 Silence detected. Stopping recording.")
                        break

    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

    return b''.join(frames)

def save_audio_to_wav(audio_bytes, filename):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(audio_bytes)
    wf.close()
    return

def transcribe_with_whisper(wav_file) -> str:
    model = whisper.load_model("base")
    print("🧠 Transcribing...", wav_file)
    result = model.transcribe(wav_file, language="en")
    print("📝 Transcription:", result["text"])
    return result["text"]

def record_speech_and_convert_to_text() -> str | None:
    audio_bytes = record_voice_until_silence()
    if len(audio_bytes) < RATE * 0.5:  # Skip too short recordings
        print("📎 Too short, skipping...\n")
        return None

    # Create a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"recordings/recording_{timestamp}.wav"
    filepath = os.path.join(os.getcwd(), filename)

    # Save and transcribe
    save_audio_to_wav(audio_bytes, filepath)
    transcribed_text = transcribe_with_whisper(filepath)

    print(f"✅ Saved: {filename}")
    return transcribed_text


# record_speech_and_convert_to_text()