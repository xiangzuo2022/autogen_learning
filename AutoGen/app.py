from os import name
import autogen
from openai import OpenAI
#from config import OPENAI_API_KEY

config_list = [
    {
        'model': 'gpt-3.5-turbo',
        'api_key': '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'
    }
]

llm_config = {
    "timeout": 600,
    "seed": 42, 
    "config_list": config_list, 
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="assistant", 
    llm_config=llm_config,
    system_message="Chief technical officer of a tech company"
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    #code_execution_config={"work_dir":"web"},
    llm_config=llm_config,
    code_execution_config=False,
    system_message="""Reply TERMINATE if the task has been solved at full satifaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
download data from https://raw.githubusercontent.com/xiangzuo2022/datasets/main/twitter_validation.csv and analyze this data and give me your insights
"""

user_proxy.initiate_chat(
    assistant, 
    message=task
)

# task2 = """
# Change the code in the file you just created to instead output numbers 1 to 200
# """

# user_proxy.initiate_chat(
#     assistant,
#     message=task2
# )
