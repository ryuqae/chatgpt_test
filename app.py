from agent import Agent
import streamlit as st

prompt = "The following is a conversation with an AI assistant. The assistant is empathetic, helpful and very friendly. Please respond to following human feelings or experiences.\n\n- Human: "


st.title("AI Chatbot")

st.write("잎클이: 안녕하세요. 잎클이입니다. 무엇이든 물어보세요.")

with st.sidebar:
    temperature = st.slider("Temperature", 0.0, 1.0, 0.9, 0.05)
    max_tokens = st.slider("Max Tokens", 10, 1000, 200, 10)
    frequency_penalty = st.slider("Frequency Penalty", 0.0, 1.0, 0.0, 0.05)
    presence_penalty = st.slider("Presence Penalty", 0.0, 1.0, 0.6, 0.05)

    engine = st.radio(
        "Engine",
        ["text-davinci-003", "text-davinci-002", "text-davinci-001", "gpt-3.5-turbo"],
    )


agent = Agent(
    prompt=prompt,
    engine=engine,
    temperature=temperature,
    max_tokens=max_tokens,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty,
)

message = st.text_area("고민거리")
st.write(agent.prompt + message)

if st.button("Send"):
    completion = agent.respond(message)
    st.write("잎클이: ", completion)
