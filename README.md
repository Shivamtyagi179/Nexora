# 🤖 Nexora AI — Offline Intelligent Assistant

> 🚀 A futuristic, privacy-first AI assistant powered entirely on local hardware — no cloud, no tracking, just pure intelligence.

---

## 🌟 Overview

**Nexora AI** is a next-generation offline AI assistant designed to run completely on your local machine. It combines **speech recognition (STT)**, **natural language processing (LLM)**, and **text-to-speech (TTS)** to create a seamless, real-time conversational experience — without relying on the internet.

Built with performance and privacy in mind, Nexora delivers **low-latency responses**, **secure data handling**, and a **futuristic user experience**.

---

## 🎯 Key Features

* 🎤 **Voice Interaction**

  * Speak naturally and interact in real-time
  * Powered by local Speech-to-Text engine

* 🧠 **Local LLM Processing**

  * No cloud APIs required
  * Fully offline AI reasoning

* 🔊 **Natural Text-to-Speech**

  * Human-like voice responses
  * Fast and lightweight synthesis

* 🧠 **Conversation Memory**

  * Remembers previous interactions
  * Context-aware responses

* 🔒 **Privacy First**

  * No data leaves your system
  * 100% local execution

* ⚡ **High Performance**

  * Optimized for low latency
  * Works smoothly even on mid-range systems

---

## 🏗️ Tech Stack

### 🧠 AI & Processing

* **Vosk** — Offline Speech Recognition (STT)
* **Local LLM (Ollama / Custom API)** — Text Generation
* **Piper TTS** — Text-to-Speech Engine

### 🎧 Audio Processing

* **sounddevice** — Microphone input handling
* **soundfile** — Audio file writing
* **pygame** — Audio playback

### 🧩 Backend Architecture

* Python (Core logic)
* Modular pipeline system
* Memory management system

---

## 📂 Project Structure

```
nexora/
│
├── audio/
│   ├── recorder.py        # 🎤 Records user voice
│   ├── player.py          # 🔊 Plays audio responses
│
├── models/
│   ├── stt.py             # 🧠 Speech-to-text (Vosk)
│   ├── tts.py             # 🔊 Text-to-speech (Piper)
│   ├── llm.py             # 🤖 LLM communication
│
├── core/
│   ├── pipeline.py        # 🔄 Main processing pipeline
│   ├── memory.py          # 🧠 Conversation memory
│   ├── config.py          # ⚙️ Configuration settings
│
├── Nexora.py              # 🚀 Main entry point
├── requirements.txt       # 📦 Dependencies
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/nexora.git
cd nexora
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Vosk Model

* Download Vosk model
* Extract into:

```
models/vosk-model/
```

### 4️⃣ Setup TTS (Piper)

* Place Piper executable + voice model in project

---

## ▶️ Usage

Run Nexora:

```bash
python Nexora.py
```

---

## 🎮 Controls

| Action         | Command               |
| -------------- | --------------------- |
| 🎤 Voice Input | Press ENTER           |
| ⌨️ Text Input  | Type message          |
| ❌ Exit         | `exit`, `quit`, `bye` |

---

## 🔄 Workflow

```
User Voice → STT → Text → LLM → Response → TTS → Audio Output
```

---

## 🧠 How It Works

1. 🎤 User speaks or types input
2. 🧠 STT converts voice → text
3. 🤖 LLM processes query
4. 🧠 Memory stores context
5. 🔊 TTS converts response → audio
6. 🎧 Audio played to user

---

## 🚧 Known Issues

* ⚠️ STT accuracy depends on microphone quality
* ⚠️ Requires proper model setup (Vosk / LLM)
* ⚠️ LLM must be running locally (e.g., Ollama)

---

## 🚀 Future Enhancements

* 🌐 Advanced UI (Futuristic Dashboard)
* 🧠 Better memory (long-term learning)
* 📱 Cross-platform support
* 🎨 3D Cinematic Interface (Three.js)
* 🤝 Multi-language support

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 💡 Vision

> Nexora is not just an assistant — it's a step toward a **fully private, offline AI ecosystem**.

---

## 👨‍💻 Author

**Shivam Tyagi**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

🔥 *Build the future. Own your AI.*
