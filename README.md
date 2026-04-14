# 🧠 Lightweight Voice-Controlled Local AI Agent

## 📌 Overview
This project is a lightweight implementation of a voice-controlled AI agent that can:
- Accept audio input (MP3/WAV)
- Process user intent
- Execute local system actions
- Display results through a simple UI

## ⚙️ Features
- 🎵 Audio file upload and playback
- 🧠 Intent detection (rule-based NLP)
- 📂 File creation
- 💻 Code generation
- 📝 Text summarization
- 💬 Basic chat response
- 🖥️ Streamlit-based UI

## 🧩 Tech Stack
- Python
- Streamlit
- Rule-based NLP (lightweight approach)

## 🚀 How It Works
1. Upload an audio file or enter text
2. Provide transcript (manual input)
3. System detects intent
4. Executes corresponding action
5. Displays result in UI

## 📁 Output Safety
All files are created inside the `output/` folder to prevent accidental system modifications.

## ⚠️ Constraints & Design Choices
Due to limited hardware and storage:
- Heavy models like Whisper were not used
- No external APIs (OpenAI, Groq)
- Implemented lightweight rule-based intent detection

This ensures:
- Low resource usage
- Offline functionality
- Clear demonstration of system pipeline

## ▶️ Run Locally

```bash
pip install streamlit
streamlit run app.py
