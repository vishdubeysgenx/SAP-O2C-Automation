from datetime import datetime
import os

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
 
from dotenv import load_dotenv
load_dotenv()

# Connection parameters for SAP OData MCP server
MCP_SERVER_URL = "http://localhost:3000/mcp/query"

# Add MCP server parameters
MCP_CONNECTION_PARAMS = {
    "base_url": MCP_SERVER_URL,
    "timeout": 30,
    "retry_attempts": 3
}

# Maintain backward compatibility
connection_params = MCP_CONNECTION_PARAMS