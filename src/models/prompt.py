from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    PromptTemplate,
)

from langchain_core.messages import SystemMessage


def create_agent_prompt():
    """ """
    another_prompt = """
    You have access to following tools

    TOOLS:
    ------

    Assistant has access to the following tools:

    {tools}

   
    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat 10 times)

    When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

    ```

    Thought: Do I need to use a tool? No

    Final Answer: [Your answer]

    ```


    Begin!

    
    conversation history:

    {chat_history}

    {input}
    
    Thought:{agent_scratchpad}
    
    Use the tool to find user style, latest fashion trend, what color and material goes
    with each other.

    Follow these steps and do all the actions with less tool usage and thought process.

    Use user search history to determine what style user likes.

    if you can't determine the style consider only user input.
    Otherwise consider both the user input and user preference and use them to

    Based on user style and input provide 3 - 4 stylish outfits that 
    has pieces that work well together.

    Give more importance to the user input.
    
    provide final recommnedation in json format with color, material and cloth name. 


    example output:
        {{
        'outfit1':[
        ],
        'outfit2':[]
        ...
        }}

    The final output should only be json object Without anything added.
    """
    human_prompt = PromptTemplate.from_template(another_prompt)

    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content="""You are a helful cloth styling assistant that helps 
                kmart customers to get best clothing styles from kmart products.
                if user asks anything other than clothing related tell them to ask
                only clothing related question.
                """
            ),
            HumanMessagePromptTemplate(prompt=human_prompt),
        ]
    )

    return prompt
