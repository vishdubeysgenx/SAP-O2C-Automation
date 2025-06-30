"""
Order to Cash Agent Team - Sales Order Management Agent

This agent specializes in sales order processing, order lifecycle management,
and customer order fulfillment in SAP.
"""

from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset   
from OrderToCashTeam.sub_agents.sales_order import prompt
from OrderToCashTeam.constants.constants import connection_params

# Sales Order management agent for order processing and lifecycle management
sales_order_agent = Agent(
    model="gemini-2.5-flash",
    name="sales_order_manager",
    description=prompt.SALES_ORDER_AGENT_DESCRIPTION,   
    instruction=prompt.SALES_ORDER_AGENT_INSTR,
    tools=[
        MCPToolset(
            connection_params=connection_params,
            tool_filter=[
                # Sales Order Management
                "getAllSalesOrders",
                "getSalesOrderByKey",
                "createSalesOrder",
                "updateSalesOrder",
                "deleteSalesOrder",
                
                # Sales Order Items
                "getAllSalesOrderItems",
                "getSalesOrderItemByKey",
                "getSalesOrderItemsBySalesOrder",
                "createSalesOrderItem",
                "updateSalesOrderItem",
                "deleteSalesOrderItem",
                
                # Sales Order Partners
                "getAllSalesOrderHeaderPartners",
                "getSalesOrderHeaderPartnersBySalesOrder",
                
                # Sales Order Schedule Lines
                "getAllSalesOrderScheduleLines", 
                "getSalesOrderScheduleLinesBySalesOrder",
                "getSalesOrderScheduleLinesBySalesOrderItem",
                
                # Sales Order Texts
                "getAllSalesOrderTexts",
                "getSalesOrderTextsBySalesOrder",
            ],
        ),  
    ]
)