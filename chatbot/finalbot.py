# import os
# from apikey import apikey
# #bring in deps
# import streamlit as st
# from langchain.llms import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, SimpleSequentialChain
# from langchain.memory import  ConversationBufferMemory



# os.environ['OPENAI_API_KEY'] = apikey
# #app framework
# st.title('Prompt based chatbot')
# prompt = st.text_input('How should i behave')

# #Prompt templates
# title_template = PromptTemplate(
#      input_variables= ['topic'],
#      template = 'Behave as a {topic} chatbot'
# )

# #Memory
# memory = ConversationBufferMemory(input_key='topic', memory_key= 'chat_history' )


# #llms
# llm = OpenAI(temperature= 0.9)
# title_chain = LLMChain(llm = llm, prompt= title_template, verbose=True)


# #show stuff on screen if there is a prompt
# if prompt:
#     response= title_chain.run( prompt)
#     st.write(response)

#     with st.expander('Message History'):
#         st.info(memory.buffer)






import os
from apikey import apikey
#bring in deps
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = apikey
#app framework
st.title('Prompt based chatbot')
prompt = st.text_input('plug in your prompt!!')

# Prompt templates
title_template = PromptTemplate(
     input_variables=['topic'],
     template='Behave as a chatbot based on the input given above {topic} '
)

prompt2 = st.text_input('How may I help you')

title_chain = LLMChain(llm=OpenAI(temperature=0.9), prompt=title_template, verbose=True)

# Prompt template for answering questions based on the first prompt
answer_template = PromptTemplate(
    input_variables=['title', 'question'],
    template='Answer the following question based on the title "{title}": {question}'
)

answer_chain = LLMChain(llm=OpenAI(temperature=0.9), prompt=answer_template, verbose=True)

# Memory
#memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')


# Show stuff on the screen if there is a prompt
if prompt:
    title_response = title_chain.run(prompt)
    st.write(title_response)

    if prompt2:
        answer_response = answer_chain.run(title=title_response, question=prompt2)
        st.write(answer_response)




