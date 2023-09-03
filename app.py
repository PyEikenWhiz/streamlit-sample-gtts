# Import the gTTS library
from gtts import gTTS
import streamlit as st

# Text to be converted to speech
text = st.text_input(label="Message", value="Hello there, welcome to the world of text-to-speech!")
st.write(text)

# Initialize gTTS object with the text and language (en for English)
lang_code = {"English":"en", "Japanese":"ja"}
selected = st.radio("Language",["English", "Japanese"])
tts = gTTS(text, lang=lang_code[selected])

if text:
  # Save the audio to a file (you can specify the filename)
  tts.save("output.mp3")
  st.write("output.mp3")
  st.audio("output.mp3")

  print("Text-to-speech conversion complete! Check the 'output.mp3' file.")
