import anthropic
import streamlit as st

st.header("Chat with Claude")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Say something to Claude"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Claude API with streaming
    client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
    response_text = ""
    with client.messages.stream(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        assistant_message = st.chat_message("assistant")
        message_placeholder = assistant_message.empty()
        for text in stream.text_stream:
            response_text += text
            message_placeholder.markdown(response_text)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})