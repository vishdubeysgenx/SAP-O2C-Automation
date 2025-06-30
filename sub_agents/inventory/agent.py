"""
Order to Cash Agent Team - Inventory Management Agent

This agent specializes in material stock management, inventory levels,
and stock availability checks across SAP plants and storage locations.
"""

from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset   
from OrderToCashTeam.sub_agents.inventory import prompt
from OrderToCashTeam.constants.constants import connection_params

# Inventory management agent for stock levels and material availability
inventory_agent = Agent(
    model="gemini-2.5-flash",
    name="inventory_manager",
    description=prompt.INVENTORY_AGENT_DESCRIPTION,   
    instruction=prompt.INVENTORY_AGENT_INSTR,
    tools=[
        MCPToolset(
            connection_params=connection_params,
            tool_filter=[
                # Material Stock Management
                "getAllMaterialStocks",
                "getMaterialStockByKey", 
                "getAllStockDetails",
                "getStockByMaterialAndPlant",
                "getStockByMaterial",
                "getUnrestrictedStock",
                
                # Material Document Operations
                "getAllMaterialDocumentHeaders",
                "getMaterialDocumentHeaderByKey",
                "getAllMaterialDocumentItems", 
                "getMaterialDocumentItemByKey",
                "getMaterialDocumentItemsByDocument",
                "createMaterialDocumentHeader",
                "createMaterialDocumentItem",
                "updateMaterialDocumentHeader",
                "updateMaterialDocumentItem",
                "cancelMaterialDocument",
                "cancelMaterialDocumentItem",
                
                # Serial Number Documents
                "getAllSerialNumberMaterialDocuments",
            ],
        ),  
    ]
)

