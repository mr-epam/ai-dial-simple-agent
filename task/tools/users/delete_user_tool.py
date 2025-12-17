from typing import Any

from task.tools.users.base import BaseUserServiceTool


class DeleteUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        #TODO: Provide tool name as `delete_users`
        ## raise NotImplementedError()
        return "delete_user"

    @property
    def description(self) -> str:
        #TODO: Provide description of this tool
        ## raise NotImplementedError()
        return "Tool for deleting a user by ID."

    @property
    def input_schema(self) -> dict[str, Any]:
        #TODO:
        # Provide tool params Schema. This tool applies user `id` (number) as a parameter and it is required
        ## raise NotImplementedError()
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "description": "The ID of the user to delete"
                }
            },
            "required": [
                "id"
            ]
        }

    def execute(self, arguments: dict[str, Any]) -> str:
        #TODO:
        # 1. Get int `id` from arguments
        # 2. Call user_client delete_user and return its results
        # 3. Optional: You can wrap it with `try-except` and return error as string `f"Error while deleting user by id: {str(e)}"`
        ## raise NotImplementedError()
        user_id = arguments.get("id")
        try:
            result = self.user_client.delete_user(user_id)
            return result
        except Exception as e:
            return f"Error while deleting user by id: {str(e)}"
