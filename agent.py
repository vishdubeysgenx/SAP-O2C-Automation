"""
Order to Cash Agent Team - Root Agent

This is the main coordinator agent for the Order to Cash (O2C) process.
It manages the entire customer order lifecycle from initial inquiry to cash collection.
"""

from google.adk.agents import Agent

from OrderToCashTeam import prompt
from OrderToCashTeam.sub_agents.inventory.agent import inventory_agent
from OrderToCashTeam.sub_agents.sales_order.agent import sales_order_agent
from OrderToCashTeam.sub_agents.product.agent import product_agent
from OrderToCashTeam.sub_agents.outbound_delivery.agent import delivery_agent

# Root agent for Order to Cash process coordination
root_agent = Agent(
    model="gemini-2.5-flash",
    name="order_to_cash_coordinator",
    description="Main coordinator for Order to Cash (O2C) business process. Manages customer orders from inquiry to delivery and manages the coordination between specialized sub-agents for different aspects of the O2C process.",
    instruction=prompt.ROOT_AGENT_INSTR,
    sub_agents=[
        product_agent,       # Product catalog management and inquiry
        inventory_agent,     # Stock levels and availability  
        sales_order_agent,   # Sales order creation and mana gement
        delivery_agent,      # Outbound delivery and fulfillment
    ],
)