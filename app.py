import asyncio
import os
from agent_framework import ChatAgent, MCPStdioTool
from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import AzureCliCredential

async def local_mcp_example():
    """Example using a local MCP server via stdio with Azure AI Agent Service."""
    databricks_token = os.getenv("DATABRICKS_TOKEN")
    databricks_url = os.getenv("DATABRICKS_URL", "https://adb-123456789.19.azuredatabricks.net/api/2.0/mcp/sql")
    
    if not databricks_token:
        raise ValueError("DATABRICKS_TOKEN environment variable is required")
    
    async with (
        AzureCliCredential() as credential,
        MCPStdioTool(
            name="databricks_sql", 
            command="npx", 
            args=["mcp-remote", databricks_url, "--header", f"Authorization: Bearer {databricks_token}"]
        ) as mcp_server,
        ChatAgent(
            chat_client=AzureAIAgentClient(async_credential=credential),
            name="DatabricksAgent",
            instructions="You are a helpful assistant that can query and analyze data using Databricks SQL.",
        ) as agent,
    ):
        result = await agent.run(
            "What is 15 * 23 + 45?", 
            tools=mcp_server
        )
        print(result.text)

if __name__ == "__main__":
    from dotenv import load_dotenv
    
    load_dotenv()
    asyncio.run(local_mcp_example())