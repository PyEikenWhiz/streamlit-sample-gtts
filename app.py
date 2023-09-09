# Import the gTTS library
from gtts import gTTS
import io
import streamlit as st

st.set_page_config(page_title="This is gTTS audio downlowader", page_icon=":loudspeaker:")

# Text to be converted to speech
text = st.text_input(label="Message", value="Hello there, welcome to the world of text-to-speech!")
st.write(text)

# Initialize gTTS object with the text and language (en for English)
lang_code = {"English":"en", "Japanese":"ja"}
selected = st.radio("Language",["English", "Japanese"])
tts = gTTS(text, lang=lang_code[selected])

if text:
  # Save the audio to a bytes-like object
  audio_bytes = io.BytesIO()
  tts.write_to_fp(audio_bytes)
  st.write("Audio!")
  st.audio(audio_bytes)

  st.write("Check the Audio file!")  # Inform the user
  st.download_button(
      label="Download Audio",
      data=audio_bytes,
      file_name="saved_audio.mp3",
      mime="mp3"
  )
  print("Text-to-speech conversion complete! ")
