# filepath: /workspaces/SAP-O2C-Automation/o2c_agent.py
from google.adk import Agent, Tool
import requests

class O2CAgent(Agent):
    def __init__(self):
        super().__init__()
        self.mcp_url = "http://localhost:3000/mcp/query"

    async def call_mcp(self, operation, parameters=None):
        response = requests.post(
            self.mcp_url,
            json={"operation": operation, "parameters": parameters}
        )
        return response.json()

    @Tool("Get all products")
    async def get_products(self):
        return await self.call_mcp("getProducts")

    @Tool("Check inventory")
    async def check_inventory(self, productId: str, plant: str):
        return await self.call_mcp("checkInventory", {"productId": productId, "plant": plant})

    @Tool("Create sales order")
    async def create_sales_order(self, customerNumber: str, items: list):
        return await self.call_mcp("createSalesOrder", {
            "customerNumber": customerNumber,
            "items": items
        })


agent = O2CAgent()        