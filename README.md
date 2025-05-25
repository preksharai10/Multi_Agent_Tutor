#  Multi-Agent AI Tutor

An AI-powered tutoring assistant built using a modular multi-agent system, inspired by Google’s Agent Development Kit (ADK) principles. This application intelligently routes academic questions to specialized agents using FastAPI, Gemini API, and Streamlit.

---

##  Live Demo

- **Frontend (Streamlit)**: [https://your-streamlit-app-url](https://multiagenttutorgit-crfjuzqeedv65nic6wqpcf.streamlit.app/)
- **Backend (FastAPI on Render)**: [https://multi-agent-tutor-smq4.onrender.com](https://multi-agent-tutor-smq4.onrender.com)
- **API Docs**: [https://multi-agent-tutor-smq4.onrender.com/docs](https://multi-agent-tutor-smq4.onrender.com/docs)

---

##  Features

- Multi-agent architecture: TutorAgent + Specialist Sub-agents
- Subject classification via keyword matching + Gemini API fallback
- Tool support:
  - MathAgent uses calculator
  - PhysicsAgent uses a constants lookup
- Gemini integration for intelligent fallback answers
- Streamlit UI with history, error handling, and clean UX

---

## How It Works

| Agent          | Role                                           | Tool/API Used       |
|----------------|----------------------------------------------  |---------------------|
| `TutorAgent`   | Classifies question and delegates task         | Keyword + Gemini    |
| `MathAgent`    | Solves math problems or calculates expressions | Calculator tool     |
| `PhysicsAgent` | Answers physics questions or constants lookup  | Constants dictionary|
| `ChemistryAgent` | Answers chemistry/general questions          | Gemini API          |

---

##  Sample Questions to Try

| Question                                  | Routed To          |
|-------------------------------------------|--------------------|
| `What is 2 + 2?`                          | MathAgent (Tool)   |
| `What is the speed of light?`             | PhysicsAgent (Tool)|
| `What is the atomic number of oxygen?`    | ChemistryAgent     |
| `Explain Newton’s second law.`            | PhysicsAgent       |
| `Who is the president of India?`          | Gemini fallback    |

---


## ⚙️ Tech Stack

- FastAPI
- Streamlit
- Gemini API (`google-generativeai`)
- Uvicorn
- Python 3.10+

---

##  Local Setup

### Backend (FastAPI)

```bash
# Clone the repo
git clone https://github.com/yourusername/multi-agent-ai-tutor.git
cd multi-agent-ai-tutor

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Then set Gemini API key:
# GEMINI_API_KEY=your-gemini-key-here

# Run the backend
uvicorn app.main:app --reload
```
### Frontend (Streamlit)
```bash
cd frontend

# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run app.py
```
Make sure API_URL in frontend/app.py is:

```bash
API_URL = "http://localhost:8000/ask"  # for local
```
For deployment, change it to:
```bash
API_URL = "https://multi-agent-tutor-smq4.onrender.com/ask"
```

## Future Improvements
- Add more agents (e.g., biology, coding)

- Use Gemini for better subject classification

- Add chat history persistence across sessions

- Upload and answer from documents (PDF, DOCX)

## Acknowledgments
- Google Generative AI (Gemini)

- FastAPI

- Streamlit

- Render
