import autogen

# https://gist.github.com/mberman84/584b470962c15930340ff49ae4e28a02
# https://www.youtube.com/watch?v=V2qZ_lgxTzg
# 太他妈的啰嗦了

# config_list = [
#     {
#         'model': 'gpt-4',
#         'api_key': 'API_KEY'
#     }
# ]

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        # "model": ["gpt4", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
        "model": ["gpt-35-turbo-16k-dep-001"]
    },
)

llm_config={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="CTO",
    llm_config=llm_config,
    system_message="Chief technical officer of a tech company"
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
Write python code to output numbers 1 to 100, and then store the code in a file named 1to100.py
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)

task2 = """
Change the code in the file you just created to instead output numbers 1 to 200
"""

user_proxy.initiate_chat(
    assistant,
    message=task2
)