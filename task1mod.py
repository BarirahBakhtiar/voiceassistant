import streamlit as st
import speech_recognition as sr
import pywhatkit
import threading

# Function to capture audio and convert it to text
def get_audio():
    try:
        # Use the microphone as the source for audio input
        with sr.Microphone() as source:
            st.write("Say something...")
            # Listen for the first phrase and extract audio data into an audio variable
            audio = recognizer.listen(source)
            # Recognize speech using Google's speech recognition service
            text = recognizer.recognize_google(audio)
            # Display what was understood
            st.write(f"You said: {text}")
            return text
    except sr.UnknownValueError:
        # Handle the error when speech is unintelligible
        st.write("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        # Handle the error if there's a problem with the Google service
        st.write(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Function to process the recognized text and perform actions based on it
def process_audio():
    # Get the text from speech
    text = get_audio()
    if text:
        # Check if the text includes the word "youtube" to play a video
        if "youtube" in text.lower():
            pywhatkit.playonyt(text)
            st.write("Playing on YouTube...")
        else:
            # If "youtube" is not mentioned, perform a web search
            pywhatkit.search(text)
            st.write("Searching on the web...")

# Setup the speech recognizer
recognizer = sr.Recognizer()

# Setup the Streamlit app
st.title("Speech Recognition App")

if st.button("Start Listening"):
    # Start a new thread to run the process_audio function
    # This ensures the Streamlit app remains responsive
    thread = threading.Thread(target=process_audio)
    thread.start()
