import os
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# 1. Load your secret API key from the .env file
load_dotenv(override=True)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# 2. Configure the look and feel of the App page
st.set_page_config(page_title="Groq AI Assistant", page_icon="🤖", layout="centered")
st.title("🤖 My Custom Groq Chatbot")
st.caption("Powered by LangChain & Groq Ultra-Fast Inference")

# 3. Initialize the Groq model inside Streamlit cache (so it stays fast)
@st.cache_resource
def get_llm():
    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY is not set. Please add it to your .env file to use the chat model."
        )
    return ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)

try:
    llm = get_llm()
except ValueError as e:
    st.error(str(e))
    llm = None

# 4. Create persistent UI Memory so the chat history doesn't erase when the page refreshes
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your real-time AI assistant. Ask me anything!"}
    ]

# 5. Render existing messages out to the screen with modern UI bubbles
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 6. Handle New User Inputs
if user_input := st.chat_input("Type your message here..."):
    
    # Display user's message instantly in the UI
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate the assistant response with a smooth loading spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                if llm is None:
                    raise RuntimeError(
                        "Chat model is not available because GROQ_API_KEY is not configured."
                    )

                # Format the full message history so the model remembers context
                formatted_history = [(m["role"], m["content"]) for m in st.session_state.messages]
                
                # Invoke the model
                response = llm.invoke(formatted_history)
                ai_response = response.content
                
                # Write response to the screen
                st.write(ai_response)
                
                # Save response to memory state
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            except Exception as e:
                st.error(f"Error fetching response: {str(e)}")