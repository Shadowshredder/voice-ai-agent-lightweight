import streamlit as st
from utils import detect_intent, create_file, write_code, summarize, chat

st.title("🧠 Lightweight Voice AI Agent")

# -------- AUDIO UPLOAD --------
audio_file = st.file_uploader("Upload MP3/WAV file", type=["mp3", "wav"])

transcribed_text = ""

if audio_file is not None:
    st.audio(audio_file)
    st.info("Audio uploaded successfully ✅")

    # Manual transcript
    transcribed_text = st.text_area("Enter transcript of audio")

# -------- TEXT INPUT --------
text_input = st.text_area("Or type directly:")

user_input = transcribed_text if transcribed_text else text_input

if st.button("Run"):

    if user_input.strip() == "":
        st.warning("Please provide input")
    else:
        intent = detect_intent(user_input)

        st.subheader("🔍 Transcribed Text")
        st.write(user_input)

        st.subheader("🧠 Detected Intent")
        st.write(intent)

        if intent == "create_file":
            result = create_file("sample.txt")

        elif intent == "write_code":
            result = write_code("code.py")

        elif intent == "summarize":
            result = summarize(user_input)

        else:
            result = chat(user_input)

        st.subheader("⚙️ Action Taken")
        st.write(intent)

        st.subheader("✅ Result")
        st.write(result)