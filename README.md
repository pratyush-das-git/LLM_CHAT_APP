# 🤖 Industry-Style LLM Chatbot

A modular, production-inspired AI chatbot built using Python and OpenAI APIs.
This project demonstrates clean architecture, environment management, logging, memory handling, and structured AI interaction — similar to patterns used in real-world GenAI systems.

---

## 🚀 Features

✅ Modular architecture
✅ Environment configuration
✅ Structured logging
✅ Conversation memory
✅ Error handling
✅ Professional system prompt
✅ Git-safe secret management

---

## 📁 Project Structure

```
LLM_CHAT_APP/
│
├── app/
│   └── main.py              # Entry point
│
├── llm/
│   ├── client.py            # OpenAI client setup
│   └── chat_service.py      # AI interaction logic
│
├── memory/
│   └── chat_memory.py       # Conversation memory
│
├── config/
│   └── settings.py          # App configuration
│
├── utils/
│   └── logger.py            # Logging utility
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/pratyush-das-git/LLM_CHAT_APP.git

cd LLM_CHAT_APP
```

---

### 2️⃣ Create virtual environment

Windows:

```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```
python -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Create environment file

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

⚠ Never commit this file.

---

## ▶ Run the Chatbot

From project root:

```
python -m app.main
```

You should see:

```
 Welcome to the AI Chatbot! Type 'exit' to quit.
```

---

## 🧠 How It Works

```
User Input
   ↓
Memory + System Prompt
   ↓
Chat Service
   ↓
OpenAI API
   ↓
Response + Logging
```

The chatbot maintains conversation context and enforces structured AI behavior.



---

## 🛠 Future Improvements

* RAG document retrieval
* FastAPI backend
* UI integration
* persistent memory
* token tracking
* streaming responses

---

## 📌 Purpose

This project is designed for learning:

* LLM integration patterns
* software architecture
* AI system design
* Git hygiene
* production mindset

---

## 👨‍💻 Author

Pratyush Das
Built as part of a GenAI engineering learning journey.

---

## ⭐ If this helped

Star the repo and keep building 🚀
