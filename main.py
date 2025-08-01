from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# Simple MCP configuration with StdioServerParameters
MCP_CONFIG = StdioServerParameters(
    command='node',
    args=['/workspaces/SAP-O2C-Automation/server.js']
)

def get_agent():
    """Function to create and return the agent instance"""
    return Agent(
        name="o2c_agent",
        description="Order to Cash Agent with MCP integration",
        model="gemini-2.5-flash",
        tools=[
            MCPToolset(
                connection_params=MCP_CONFIG,
                tool_filter=[
                    'getProducts',
                    'checkInventory', 
                    'createSalesOrder'
                ]
            )
        ]
    )

# Create agent instance
agent = get_agent()

if __name__ == "__main__":
    agent = agent