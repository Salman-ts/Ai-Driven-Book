# Physical AI & Humanoid Robotics: An Agent-Native Educational Platform

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

An advanced, AI-powered educational book platform designed to teach **Physical AI** and **Humanoid Robotics**. This system goes beyond static text, offering an interactive learning experience with Retrieval Augmented Generation (RAG), personalized content adaptation, and agentic workflows.

## 🚀 Key Features

*   **📚 Agent-Native Architecture:** Built from the ground up to integrate AI agents as first-class citizens in the learning process.
*   **🤖 RAG Chatbot ("AI Helper"):** A context-aware chatbot capable of answering specific questions based on the book's content, powered by Qdrant and OpenAI.
*   **✨ Adaptive Personalization:** Dynamically rewrites chapter content to match the learner's profile (e.g., "Beginner" vs. "Expert", "Software-focus" vs. "Hardware-focus").
*   **🌐 Urdu Translation Mode:** One-click translation of technical content into Urdu, preserving code blocks and formatting.
*   **🔐 Authentication & Profiles:** User signup/signin with profile management to track learning goals and skills (backed by Neon Postgres).
*   **🏆 Gamification:** Earn points for completing chapters and interacting with AI features.

## 🛠️ Tech Stack

### Frontend
*   **Framework:** [Docusaurus 3](https://docusaurus.io/) (React-based static site generator).
*   **Styling:** Custom CSS with "Google Blue" Light Mode and "AI Native" Slate/Violet Dark Mode.
*   **Components:** Custom React components for Chat Widget and Chapter Controls.

### Backend
*   **API:** [FastAPI](https://fastapi.tiangolo.com/) (Python).
*   **Database:** [Neon Postgres](https://neon.tech/) (Serverless PostgreSQL).
*   **Vector DB:** [Qdrant](https://qdrant.tech/) (for RAG embeddings).
*   **AI/LLM:** OpenAI GPT-4 Turbo & Assistants API.
*   **Agents:** Custom `ChatKitAgent` implementation wrapping OpenAI Beta Assistants.

## 📦 Installation & Setup

### Prerequisites
*   Node.js 18+
*   Python 3.9+
*   Git

### 1. Clone the Repository
```bash
git clone https://github.com/Salman-ts/Ai-Driven-Book.git
cd Ai-Driven-Book
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
# source venv/bin/activate

pip install -r requirements.txt
```

**Configuration:**
Rename `env_example` to `.env` and fill in your credentials:
```env
OPENAI_API_KEY=sk-...
QDRANT_URL=https://...
QDRANT_API_KEY=...
NEON_DSN=postgresql://...
```

**Run Server:**
```bash
uvicorn main:app --reload
```

### 3. Frontend Setup
Open a new terminal in the root directory:
```bash
npm install
npm start
```
The application will launch at `http://localhost:3000/ai-book/`.

## 🧪 Testing

### Automated Agent Tests
```bash
# In backend directory
pytest tests/
```

### Manual Verification
```bash
# Test DocGen Agent
python -m scripts.test_agent_manual
```

### Frontend Demo
Visit `http://localhost:3000/ai-book/demo` to see the AI components in isolation.

## 🤝 Contribution
1. Fork the repo.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
