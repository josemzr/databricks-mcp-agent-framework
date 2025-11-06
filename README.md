# Databricks MCP with Azure AI Agent Service

This sample demonstrates how to use Azure AI Agent Service with a local MCP (Model Context Protocol) server connected to Databricks SQL via STDIO.

## Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Node.js and npm (for `npx` command)
- Azure CLI installed and logged in (`az login`)
- Azure AI Foundry resource with a deployed model
- Databricks workspace with API token

## Setup

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Configure environment variables:**
   
   Create a `.env` file in the project root with the following variables:
   ```env
   # Azure AI Agent Service
   AZURE_AI_PROJECT_ENDPOINT=your_azure_ai_endpoint
   AZURE_AI_MODEL_DEPLOYMENT_NAME=your_model_deployment_name
   
   # Databricks
   DATABRICKS_TOKEN=your_databricks_token
   DATABRICKS_URL=https://your-databricks-instance.azuredatabricks.net/api/2.0/mcp/sql
   ```

3. **Login to Azure CLI:**
   ```bash
   az login
   ```

## Running the Sample

Execute the sample using uv:

```bash
uv run app.py
```

## How It Works

The sample:
1. Connects to Azure AI Agent Service using Azure CLI credentials
2. Establishes a STDIO connection to Databricks SQL via MCP using `npx mcp-remote`
3. Creates an agent that can query and analyze data using Databricks SQL
4. Runs a sample query through the agent

## Architecture

- **Agent Framework**: Uses Microsoft Agent Framework for agent orchestration
- **MCP Integration**: MCPStdioTool connects to Databricks via local MCP server
- **Authentication**: Azure CLI credentials for Azure AI, bearer token for Databricks

## Files

- `app.py` - Main application using Azure AI Agent Service
- `azure_ai_with_mcp.py` - Reference examples for MCP integration patterns
- `.env` - Environment variables (not tracked in git)
- `.gitignore` - Excludes sensitive files from version control
