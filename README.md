# Assignment 27: Chatbots with Conversation History using LangChain

A simple Python chatbot assignment demonstrating message types, prompt placeholders, chat history, trimming old messages, and contextual Q&A.

## Run on Windows / VS Code

1. Install Python 3.10 or newer.
2. Extract this ZIP and open this folder in VS Code.
3. Open `.env` and replace `your_groq_api_key_here` with your own key from https://console.groq.com/ . Keep the key private.
4. Open the VS Code terminal and run:

```bash
python -m pip install -r requirements.txt
python chatbot.py
```

5. Ask questions. Type `exit` to stop the chatbot.

The program automatically reads `GROQ_API_KEY` from `.env` using `python-dotenv`.

## Included files
- `chatbot.py` — chatbot with conversation history and trimming
- `.env` — API key configuration template (add your own key)
- `.gitignore` — keeps `.env` and the virtual environment out of version control
- `requirements.txt` — required packages
- `concepts_and_observations.md` — short assignment answers

Note: The `.venv` folder is intentionally not included. Create your own environment on your computer; this keeps the ZIP smaller and avoids machine-specific files.
