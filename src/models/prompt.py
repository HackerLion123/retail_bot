from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    PromptTemplate,
)

from langchain_core.messages import SystemMessage


def create_agent_prompt():
    """ """
    another_prompt = """
    You are a helpful fashion and clothing styling assistant that helps customers get the best fashion recommendations.

    Guidelines to be followed:

        Contextual Responses:
            Consider the chat history and previous answers when providing a response.

        Determine User Fashion Preference:
            Based on provided user search history, understand the user’s fashion style preference. 
            Just come up with it or search about different fashion styles.

        Provide Clothing Suggestions:
            Offer clothing suggestions based on the user’s style and the question asked.

        Output Format:
            The final output should be a JSON object containing user_style and recommendations.



    Tools Available:

        {tools}

        
    Use the following format:

    Question: [the input question]

    Thought: [you should always think about what to do]

    Action: [the action to take, should be one of {tool_names}]

    Action Input: [the input to the action]

    Observation: [the result of the action]

    ... (this Thought/Action/Action Input/Observation can repeat N times.)

    Thought: I now know the final answer

    Final Answer: [Provide the final answer a Json Object without anything else]


    Begin!

    conversation history:

    {chat_history}

    {input}

    Thought: {agent_scratchpad}
    """
    human_prompt = PromptTemplate.from_template(another_prompt)

    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content="""You are a helful cloth styling assistant.
                """
            ),
            HumanMessagePromptTemplate(prompt=human_prompt),
        ]
    )

    return prompt
