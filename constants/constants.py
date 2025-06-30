from datetime import datetime
import os

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
 
from dotenv import load_dotenv
load_dotenv()

# Connection parameters for SAP OData MCP server
MCP_CONNECTION_PARAMS = StdioServerParameters(
    command='node',
    args=["/Users/felipe/Documents/coding/sap-odata-mcp/build/index.js"]
)

# Maintain backward compatibility
connection_params = MCP_CONNECTION_PARAMS