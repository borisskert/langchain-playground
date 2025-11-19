import os

import streamlit as st
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from tools.hardcoded import get_weather as get_weather_hardcoded
from tools.weatherapi_com import get_weather as get_weather_api

tools = []

if os.environ.get("WEATHER_API_KEY") is not None:
    tools.append(get_weather_api)
else:
    tools.append(get_weather_hardcoded)

llm = ChatOllama(
    model="gpt-oss:20b",
    validate_model_on_init=True,
    temperature=0,
)

agent = create_agent(
    llm,
    tools=tools,
)

st.title('Tool Usage and Function calls.')
prompt = st.chat_input("Say something...")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "ai", "content": "Hello 👋"}
    ]

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state["messages"].append({"role": "user", "content": prompt})

    response = agent.invoke({"messages": st.session_state["messages"]})

    ai_msg = response["messages"][-1].content

    st.session_state["messages"].append({"role": "ai", "content": ai_msg})

    with st.chat_message("ai"):
        st.write(ai_msg)
