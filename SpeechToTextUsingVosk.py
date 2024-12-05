import os
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

# Path to the VOSK model directory
MODEL_PATH = "models/vosk-model-small-en-us-0.15"

# Ensure the model exists
if not os.path.exists(MODEL_PATH):
    print("Please download the VOSK model from https://alphacephei.com/vosk/models or please check the path")
    exit(1)

# Load the VOSK model
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)
audio_queue = queue.Queue()

# Callback function to capture audio
def audio_callback(indata, frames, time, status):
    if status:
        print(f"Audio error: {status}")
    audio_queue.put(bytes(indata))

# Function to process real-time audio
def process_audio():
    print("Listening... Speak into the microphone.")
    partial_text = ""
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=audio_callback):
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                # Print the final recognized sentence
                final_result = recognizer.Result()
                text = eval(final_result).get("text", "")
                if text:
                    print(f"\rFinal Sentence: {text}", end="\n")
                    partial_text = ""  # Reset for the next sentence
            else:
                # Print the recognized words in the same line
                partial_result = recognizer.PartialResult()
                word = eval(partial_result).get("partial", "")
                if word and word != partial_text:  # Avoid duplicate updates
                    print(f"\rWord: {word}", end="", flush=True)
                    partial_text = word

# Main function
if __name__ == "__main__":
    try:
        process_audio()
    except KeyboardInterrupt:
        print("\nProgram terminated.")
    except Exception as e:
        print(f"An error occurred: {e}")
