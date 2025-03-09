# Simple AI Chatbot

## Overview
This is a simple AI chatbot powered by Gemini (or OpenAI) that engages in interactive conversations with users. The chatbot is built using Python and Streamlit for the interface, making it easy to deploy and use.

## Features
- Interactive conversation loop
- AI-powered responses using Gemini API
- Simple and lightweight Streamlit UI
- Easily customizable for different use cases

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/shivs7278/chatbot.git
   cd chatbot
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API key:
   - Create a `.env` file and add your Gemini API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

Run the chatbot with Streamlit:
```bash
streamlit run app.py
```

## File Structure
```
chatbot/
│── app.py            # Main Streamlit app
│── .env              # API key (not to be shared)
```

## Customization
- Modify `chatbot.py` to change the AI model or response logic.
- Update the Streamlit UI in `app.py` for a different user experience.

## License
This project is open-source

---
### Contributors
Made with ❤️ by [Shivs]

here's the example:

<img width="887" alt="shivsai" src="https://github.com/user-attachments/assets/c9c32dc7-80c2-4a10-835d-e70ccfa08b5c" />

