# Groq Chatbot

A Streamlit-based chatbot UI using `langchain-groq` and the Groq API.

## Files

- `ui.py` — Streamlit app source code
- `requirement.txt` — Python dependencies
- `.gitignore` — ignores virtual env files, caches, and secrets

## Setup

1. Install Python 3.12+.
2. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirement.txt
   ```
4. Create a `.env` file with your Groq API key:
   ```env
   GROQ_API_KEY=your_actual_key_here
   ```

## Run the app

```powershell
.\.venv\Scripts\python.exe -m streamlit run ui.py --server.address 127.0.0.1 --server.port 8501
```

Then open `http://127.0.0.1:8501` in your browser.

## Publish to GitHub

1. Install Git on your computer.
2. Create a new GitHub repository on github.com.
3. In this project folder, run:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

## Notes

- Do not commit the `.env` file.
- If you want a public URL, use a hosting service or a tunnel like `ngrok`.
