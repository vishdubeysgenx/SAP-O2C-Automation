"""
Product Agent - Order to Cash Sub-Agent

Handles all product-related operations including product catalog management,
product information retrieval, and product data management within the O2C process.
"""

from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from utils.mcp_client import MCPClient

from OrderToCashTeam.sub_agents.product import prompt
from OrderToCashTeam.constants.constants import MCP_CONNECTION_PARAMS

# Product agent specialized for product catalog management
product_agent = Agent(
    model="gemini-2.5-flash",
    name="product_specialist",
    description="Specialized agent for product catalog management and product information queries. Handles product master data, descriptions, plant-specific data, and product inquiries within the Order to Cash process.",
    instruction=prompt.PRODUCT_AGENT_INSTR,
    tools=[
        MCPToolset(
            connection_params=MCP_CONNECTION_PARAMS,
            tool_filter=[
                # Product Management
                'getAllProducts',
                'getProductByKey', 
                'createProduct',
                'updateProduct',
                # Product Descriptions
                'getAllProductDescriptions',
                'getProductDescriptionsByProduct',
                # Product Plants
                'getAllProductPlants',
                'getProductPlantsByProduct',
            ]
        )
    ],
)

class ProductAgent:
    def __init__(self):
        self.mcp_client = MCPClient()
        self.name = "Product Agent"

    async def get_all_products(self):
        return await self.mcp_client.execute_operation("getProducts")
    
    async def get_product_details(self, product_id: str):
        return await self.mcp_client.execute_operation(
            "getProductByKey", 
            {"productId": product_id}
        )