from agent import Agent
import streamlit as st


st.title("AI Chatbot")

st.write("잎클이: 안녕하세요. 잎클이입니다. 어떤 고민이든 나눠보아요.")

with st.sidebar:
    temperature = st.slider("Temperature", 0.0, 1.0, 0.9, 0.05)
    max_tokens = st.slider("Max Tokens", 10, 1000, 200, 10)
    frequency_penalty = st.slider("Frequency Penalty", 0.0, 1.0, 0.0, 0.05)
    presence_penalty = st.slider("Presence Penalty", 0.0, 1.0, 0.6, 0.05)

    engine = st.radio(
        "Engine",
        [
            "gpt-3.5-turbo",
        ],
    )


agent = Agent(
    engine=engine,
    temperature=temperature,
    max_tokens=max_tokens,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty,
)

gaslighting = st.text_area("가스라이팅")

message = st.text_area("고민거리")

if st.button("Send"):
    responses = []
    completion = agent.respond(message=message, gaslighting=gaslighting)
    st.write(f"잎클이: {completion['message']['content']}")
