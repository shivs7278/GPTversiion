import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="your api key")  # Replace with your actual API key

# Initialize the model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit UI
st.title("Chatbot with Shivs AI")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me something...")

if user_input:
    # Append user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate response from Gemini model
    response = model.generate_content(user_input)
    bot_reply = response.text
    
    # Append response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
