from google.adk.agents import Agent
from sub_agents.outbound_delivery.agent import delivery_agent
from sub_agents.product.agent import product_agent
from sub_agents.inventory.agent import inventory_agent
from sub_agents.sales_order.agent import sales_order_agent

def create_agent():
    return Agent(
        name="o2c_coordinator",
        description="Order to Cash Process Coordinator",
        model="gemini-2.5-flash",
        sub_agents=[
            delivery_agent,
            product_agent,
            inventory_agent,
            sales_order_agent
        ]
    )

# Export the agent creation function
get_agent = create_agent