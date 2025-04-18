# MCP Chat Bot

This project provides an interactive chat application powered by MCPAgent with built-in conversation memory and web search capabilities. It supports two modes of usage: a command-line interface (CLI) and a Streamlit web interface.

---

## Prerequisites

- Python 3.10 or higher
- A valid `GROQ_API_KEY` environment variable set in your environment or in a `.env` file
- A configuration file named `config.json` in the project root directory

---

## CLI Usage

The CLI chat application allows you to interact with the MCPAgent directly from your terminal.

### How to run

```bash
python app.py
```

### Commands

- Type your message and press Enter to send it to the assistant.
- Type `exit` or `quit` to end the conversation.
- Type `clear` to clear the conversation history.

---

## Streamlit Usage

The Streamlit app provides a web-based chat interface with conversation memory.

### How to run

```bash
streamlit run app_streamlit.py
```

### User Interface

- **Input box:** Type your message here.
- **Send button:** Send your message to the assistant.
- **Clear button:** Clear the conversation history.

The chat history is displayed below the input area, showing both your messages and the assistant's responses.

---

## Notes

- Both CLI and Streamlit modes use built-in conversation memory to maintain context.
- Clearing the conversation history resets the memory for a fresh start.
- Ensure your `GROQ_API_KEY` is valid and your `config.json` is properly configured before running the applications.

---

Enjoy chatting with MCPAgent!
