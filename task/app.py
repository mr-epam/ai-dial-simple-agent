import os

import asyncio

#from task.client import DialClient
from task.async_client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role
from task.prompts import SYSTEM_PROMPT
from task.tools.users.create_user_tool import CreateUserTool
from task.tools.users.delete_user_tool import DeleteUserTool
from task.tools.users.get_user_by_id_tool import GetUserByIdTool
from task.tools.users.search_users_tool import SearchUsersTool
from task.tools.users.update_user_tool import UpdateUserTool
from task.tools.users.user_client import UserClient
from task.tools.web_search import WebSearchTool

DIAL_ENDPOINT = "https://ai-proxy.lab.epam.com"
API_KEY = os.getenv('DIAL_API_KEY')

async def main():
    deployment_name = "gpt-4o"
    #TODO:
    # 1. Create UserClient
    # 2. Create DialClient with all tools (WebSearchTool, GetUserByIdTool, SearchUsersTool, CreateUserTool, UpdateUserTool, DeleteUserTool)
    # 3. Create Conversation and add there first System message with SYSTEM_PROMPT (you need to write it in task.prompts#SYSTEM_PROMPT)
    # 4. Run infinite loop and in loop and:
    #    - get user input from terminal (`input("> ").strip()`)
    #    - Add User message to Conversation
    #    - Call DialClient with conversation history
    #    - Add Assistant message to Conversation and print its content
    ## raise NotImplementedError()
    user_client = UserClient()
    tools = [
        WebSearchTool( api_key=API_KEY, endpoint=DIAL_ENDPOINT),
        GetUserByIdTool(user_client=user_client),
        SearchUsersTool(user_client=user_client),
        CreateUserTool(user_client=user_client),
        UpdateUserTool(user_client=user_client),
        DeleteUserTool(user_client=user_client)
    ]
    dial_client = DialClient(
        endpoint=DIAL_ENDPOINT,
        deployment_name=deployment_name,
        api_key=API_KEY,
        tools=tools
    )

    conversation = Conversation()
    conversation.add_message(Message(role=Role.SYSTEM, content=SYSTEM_PROMPT))

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            print("Exiting the chat. Goodbye!")
            break

        conversation.add_message(Message(role=Role.USER, content=user_input))

        # assistant_message = dial_client.get_completion(conversation.messages) # task.client
        assistant_message = await dial_client.get_completion(conversation.messages) # task.async_client | AsyncDial with stream=True

        conversation.add_message(assistant_message)

        print("🤖:", assistant_message.content)
        print("=" * 100)
        print()


asyncio.run(
    main()
)

#TODO:
# Request sample:
# Add Andrej Karpathy as a new user