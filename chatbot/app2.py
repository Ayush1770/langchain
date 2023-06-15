import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

st.title(' Demo Chatbot')
prompt = st.text_input('Plug in your prompt ')


llm = OpenAI(temperature=0.9)

if prompt:
    response = llm(prompt)
    st.write(response)