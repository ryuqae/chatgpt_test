from agent import Agent
import streamlit as st

prompt = "The following is a conversation with an AI assistant. The assistant is empathetic, helpful and very friendly.\n\n"

agent = Agent(prompt)

st.title("AI Chatbot")

message = st.text_area("고민거리")

if st.button("Send"):
    completion = agent.respond(message + "잎클이: ")
    st.write("잎클이: ", completion)
