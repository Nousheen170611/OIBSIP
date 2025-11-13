import sounddevice as sd
import wavio
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen(seconds=4, filename="input.wav"):
    """Record from microphone and return recognized text."""
    recognizer = sr.Recognizer()
    fs = 44100
    channels = 1
    try:
        print(f"\n🎤 Recording for {seconds} seconds... Speak now.")
        audio_data = sd.rec(int(seconds * fs), samplerate=fs, channels=channels)
        sd.wait()
        wavio.write(filename, audio_data, fs, sampwidth=2)
    except Exception as e:
        speak("Could not access the microphone.")
        print("Recording error:", e)
        return ""

    try:
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)
        print("🧠 Recognizing...")
        command = recognizer.recognize_google(audio, language="en-in")
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Network error. Please check your internet connection.")
        return ""
    finally:
        if os.path.exists(filename):
            os.remove(filename)

def main():
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = listen(seconds=4)
        if command == "":
            continue

        if "hello" in command:
            speak("Hi there! How are you?")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")
        elif "date" in command:
            today = datetime.datetime.now().strftime("%A, %d %B %Y")
            speak(f"Today is {today}")
        elif "search" in command:
            speak("What should I search for?")
            query = listen(seconds=4)
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Here are the results for {query}")
        elif "bye" in command or "exit" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm sorry, I don't know that command yet.")

if __name__ == "__main__":
    main()
 