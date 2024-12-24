import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# initialise translator text to speech engine
translator = Translator()
tts_engine = pyttsx3.init()

# function to speak, translated text
def speak_text(text, language):
    tts_engine.setProperty('voice', 'com.apple.speech.synthesis.voice.alex' if language == 'en' else 'com.apple.speech.synthesis.voice.thomas')  # Adjust for language if needed
    tts_engine.say(text)
    tts_engine.runAndWait()

# function to recognize speech, translate
def recognize_and_translate():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening Speak now!")
        try:
            # capture audio input
            audio = recognizer.listen(source)
            print("Recognizing")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # translate text
            target_language = input("Enter target language code (e.g., 'telugu' and 'hindi'): ")
            translation = translator.translate(text, dest=target_language)
            print(f"Translated ({target_language}): {translation.text}")

            # Speak translated text
            speak_text(translation.text, target_language)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Welcome to Real-Time Language Assistant!")
    while True:
        recognize_and_translate()
        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont != "yes":
            print("bye!")
            break
