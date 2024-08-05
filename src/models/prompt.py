from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


bos = "<|begin_of_text|>"
header_start = "<|start_header_id|>"
header_end = "<|end_header_id|>"
eos = "<|eot_id|>"


def create_agent_prompt():
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                """You are a helful cloth styling assistant that helps kmart customers to get best clothing styles.
                You have access to DuckDuckGoRun Tool which you can use to understand different fashion trends 
                and also find which color or material goes with what 
                and a reteriver tool that can find kmart products and it will give it's details.
                Don't answer anything not releated to cloth styling.
                """
            )
        ]
    )

    inital_search_prompt = """
    You are a cloth styling assistant that provide clothing recommendation based on user query.

    You have access to DuckDuckGoSearchRun tool which you can use to search web on good trends and
    matching colors to use for style recommendation.

    You will have following 3 inputs:

    User's Past 4 purchases
    {user_history}

    User's Past 3 Search
    {user_search_history}

    User Query:
    {user_query}

    Now, 
        
    If you haven't provided recommendation already
    follow these instrustions step by step and don't miss any step.

    1. Based on the user's purchase and search history determine user's gender.
    2. Based on the user's purchase, gender and search history determine user's style preference.
        eg: casual, business casual, vintage, street wear, punk, girly girl etc.
    3. Now use web to search for latest trends in user's style preference category.
    4. Now consider user's search query and find styles that matches with user search query.
    5. The recommendation you provide should be name of the clothing item, color material.


    If you have provided recommendation     
    """

    refine_prompt = """

    """
