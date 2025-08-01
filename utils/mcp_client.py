import requests
from constants.constants import MCP_CONNECTION_PARAMS

class MCPClient:
    def __init__(self):
        self.base_url = MCP_CONNECTION_PARAMS["base_url"]
        self.timeout = MCP_CONNECTION_PARAMS["timeout"]
        
    async def execute_operation(self, operation: str, parameters: dict = None):
        try:
            response = requests.post(
                self.base_url,
                json={"operation": operation, "parameters": parameters},
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"MCP Operation failed: {str(e)}")
            return {"success": False, "error": str(e)}