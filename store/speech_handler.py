# Example using a pre-trained speech-to-text model from Hugging Face's Transformers library
from transformers import pipeline
import speech_recognition as sr


def transcribe_audio_with_ai():
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise before recording
        recognizer.adjust_for_ambient_noise(source)

        # Record audio
        audio = recognizer.listen(source)

    # Use the automatic-speech-recognition pipeline for transcription
    recognizer = pipeline("automatic-speech-recognition")
    transcription = recognizer(audio)

    return transcription

# Example usage
user_command = transcribe_audio_with_ai()
print("User command:", user_command)


# Example using a pre-trained intent recognition model from Hugging Face's Transformers library
def process_command_with_ai(transcription):
    intent_recognizer = pipeline("zero-shot-classification")
    candidate_labels = ["navigate_home", "click_button", "search", "play_music", "send_message"]
    result = intent_recognizer(transcription, candidate_labels)
    intent = result["labels"][0] if result["scores"][0] > 0.5 else "unknown"
    return intent

# Example usage
user_transcription = "Navigate to the home page"
intent = process_command_with_ai(user_transcription)
print("Intent:", intent)
