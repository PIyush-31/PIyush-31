import speech_recognition as sr
import requests
from transformers import pipeline
import wave 

def transcribe_audio(audio_data, model_name, api_token):
    """Transcribes audio data using a Hugging Face model and API.

    Args:
        audio_data: The audio data to be transcribed (assumed to be in WAV format).
        model_name: The name of the Hugging Face model to use.
        api_token: Your Hugging Face API token.

    Returns:
        The transcription of the audio data.
    """

    with wave.open(audio_data, 'rb') as wav_file:
        # Get frame rate and number of frames
        frame_rate = wav_file.getframerate()
        frames = wav_file.getnframes()
        # Extract raw audio bytes
        audio_bytes = wav_file.readframes(frames)

    # Convert raw bytes to a list (required by Hugging Face API)
    audio_list = list(audio_bytes)

    url = "https://api-inference.huggingface.co/models/" + 'meta-llama/Meta-Llama-3.1-70B-Instruc'
    headers = {"Authorization": f"Bearer {'8ffa22d8-eef2-409f-a6f6-6e4bad75646a16ff93'}"}
    data = {"inputs": audio_list}  # Use a list instead of raw bytes

    try:
        response = requests.post(url, headers=headers, json=data)
        transcription = response.json()[0]["text"]
        return transcription
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None
def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio_data = recognizer.listen(source)

    # Choose a model and API token
    model_name = "meta-llama/Meta-Llama-3.1-70B-Instruc"  # Replace with your desired model
    api_token = "8ffa22d8-eef2-409f-a6f6-6e4bad75646a16ff93"  # Replace with your API token

    # Transcribe the audio
    transcription = transcribe_audio(audio_data, model_name, api_token)

    if transcription:
        print("You said:", transcription)
    else:
        print("Transcription failed.")

if __name__ == "__main__":
    main()