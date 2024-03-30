import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from IPython.display import Image
import autogen
import os
import streamlit as st

def agent(query):

    config_list = [
        {
            'model': 'gpt-3.5-turbo',
            'api_key': os.environ["OPENAI_API_KEY"]
        }
    ]

    llm_config = {
        "timeout": 600,
        "seed": 42, 
        "config_list": config_list, 
        "temperature": 0
    }

    Emily = autogen.UserProxyAgent(
        name="Emily",
        system_message="A human admin.",
        code_execution_config={
            "last_n_messages": 3,
            "work_dir": "groupchat",
            "use_docker": False,
        },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
        human_input_mode="NEVER",
    )
    coder = autogen.AssistantAgent(
        name="Coder",  # the default assistant agent is capable of solving problems with code
        system_message="""Coder. You are a software developer with experience in Python. You are proficient in data manipulation, analysis, and visualization using libraries like Pandas, NumPy, and Matplotlib. You are also familiar with machine learning concepts and libraries like scikit-learn and TensorFlow. execute the code.""",
        llm_config=llm_config,
    )
    data_scientist = autogen.AssistantAgent(
        name="data_scientist",
        system_message="""data_scientist. You are a experienced data scientist with knowledge in Machine Learning Modelling, Statistics and Experimentation. My skills also cover Reporting, Business Insight, Storytelling and Data Visualization.
        - Data Collection and Cleaning: Acquiring, processing, and cleaning large datasets to ensure data quality.
        - Data Collection and Cleaning: Acquiring, processing, and cleaning large datasets to ensure data quality.
        - Exploratory Data Analysis (EDA): Understanding the data through visualization and statistical summaries.
        - Feature Engineering: Creating new features from existing data to enhance model performance.
        - Model Selection and Training: Choosing appropriate machine learning models and training them on the data.
        - Model Evaluation and Validation: Assessing model performance and ensuring its generalizability.
        - Deployment and Monitoring: Implementing models in production and monitoring their performance over time.
        Data Scientists use a variety of tools and programming languages such as Python, R, SQL, and libraries like Pandas, NumPy, scikit-learn, and TensorFlow. They are proficient in techniques like regression, classification, clustering, and deep learning.
    Do not suggest code.
    Finally, based on the critique above, suggest a concrete list of actions that the coder should take to improve the code.
    """,
        llm_config=llm_config,
    )

    groupchat = autogen.GroupChat(agents=[Emily, coder, data_scientist], messages=[], max_round=20)
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    # start chat
    Emily.initiate_chat(manager,message= query)
        #"read data diabetes.csv from directory /Users/emilyzuo/Desktop/agent/autogen_learning/groupchat and do a classification to generate a model to predict the Outcome column. Save the model to a file. Use the same input data to predict the class column and save the predictions to a file. use automl to get the best model.",
    
    # type exit to terminate the chat
    return coder.chat_messages_for_summary
def main():
    st.set_page_config(page_title="AI Assistant Agent", page_icon=":dolphin:")

    st.header("AI Agent for Data Scientist -- TunyAI", divider='rainbow')
    st.header("AI Agent :blue[Assistant] :dolphin:")


    query = st.text_input("questions and requirements：")

    if query:
         st.write(f"begin data analysis 【 {query}】 pleawse wait")

         result = agent(query)

         st.info(result)


def print_hi(message):
    print('===============================================================')
    print(f'{message}')
    #print(f'OpenAI key: {openai_api_key}')
    #print(f'Serper key: {serper_api_key}')
    #print(f'Browserless key: {browserless_api_key}')
    print('===============================================================')

if __name__ == '__main__':
    print_hi('AI Agent for Data Scientist -- TunyAI')
    main()