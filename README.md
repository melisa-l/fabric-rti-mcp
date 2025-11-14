[![Install with UVX in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Fabric_RTI_MCP_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=ms-fabric-rti&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22microsoft-fabric-rti-mcp%22%5D%7D) [![GitHub](https://img.shields.io/badge/GitHub-fabric--rti--mcp-181717?style=flat-square&logo=github)](https://github.com/melisa-l/fabric-rti-mcp) [![PyPI Downloads](https://static.pepy.tech/badge/microsoft-fabric-rti-mcp)](https://pepy.tech/projects/microsoft-fabric-rti-mcp)

## 🎯 Overview

A Model Context Protocol (MCP) server implementation for [Microsoft Fabric Real-Time Intelligence (RTI)](https://aka.ms/fabricrti). 
This server enables AI agents to interact with Fabric RTI services by providing tools through the MCP interface, allowing for seamless data querying and analysis capabilities.

> [!NOTE]  
> This project is in Public Preview and implementation may significantly change prior to General Availability.

### 📦 Installation Options

- **🚀 Quick Start (GitHub)**: Clone and install locally for latest features - [See 5-minute guide](QUICKSTART.md) or [detailed instructions below](#-install-from-github-recommended-for-development)
- **📦 PyPI Package**: Install via pip for stable releases - [See PyPI instructions](#-alternative-install-from-pypi-pip)
- **🔧 Development**: Full setup for contributing and debugging - [See debugging guide](#-debugging-the-mcp-server-locally)

### 🔍 How It Works

The Fabric RTI MCP Server acts as a bridge between AI agents and Microsoft Fabric RTI services:

- 🔄 **MCP Protocol**: Uses the Model Context Protocol to expose Fabric RTI capabilities as tools
- 🏗️ **Natural Language to KQL**: AI agents can translate natural language requests into KQL queries
- 💡 **Secure Authentication**: Leverages Azure Identity for seamless, secure access to your resources
- ⚡ **Real-time Data Access**: Direct connection to Eventhouse and Eventstreams for live data analysis

### ✨ Supported Services

**Eventhouse (Kusto)**: Execute KQL queries against Microsoft Fabric RTI [Eventhouse](https://aka.ms/eventhouse) and [Azure Data Explorer (ADX)](https://aka.ms/adx).

**Eventstreams**: Manage Microsoft Fabric [Eventstreams](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/eventstream/eventstream-introduction) for real-time data processing:
- List Eventstreams in workspaces
- Get Eventstream details and definitions

## 🚧 Coming soon
- **Activator**
- **Other RTI items**

### 🔍 Example Prompts

**Eventhouse Analytics:**
- "Get databases in my Eventhouse"
- "Sample 10 rows from table 'StormEvents' in Eventhouse"
- "What can you tell me about StormEvents data?"
- "Analyze the StormEvents to come up with trend analysis across past 10 years of data"
- "Analyze the commands in 'CommandExecution' table and categorize them as low/medium/high risks"

**SQL Lakehouse Analytics:**
- "What tables are in my SQL lakehouse?"
- "Show me the schema of table 'MyTable' in the lakehouse"
- "List all tables and their columns in my lakehouse"

**Eventstream Management:**
- "List all Eventstreams in my workspace"
- "Show me the details of my IoT data Eventstream"


### Available tools 

#### SQL Lakehouse - 2 Tools:
- **`sql_list_lakehouse_tables`** - List all tables in a Fabric SQL lakehouse
- **`sql_get_table_schema`** - Get detailed schema information for a specific table in the lakehouse

#### Eventhouse (Kusto) - 12 Tools:
- **`kusto_known_services`** - List all available Kusto services configured in the MCP
- **`kusto_query`** - Execute KQL queries on the specified database
- **`kusto_command`** - Execute Kusto management commands (destructive operations)
- **`kusto_list_databases`** - List all databases in the Kusto cluster
- **`kusto_list_tables`** - List all tables in a specified database
- **`kusto_get_entities_schema`** - Get schema information for all entities (tables, materialized views, functions) in a database
- **`kusto_get_table_schema`** - Get detailed schema information for a specific table
- **`kusto_get_function_schema`** - Get schema information for a specific function, including parameters and output schema
- **`kusto_sample_table_data`** - Retrieve random sample records from a specified table
- **`kusto_sample_function_data`** - Retrieve random sample records from the result of a function call
- **`kusto_ingest_inline_into_table`** - Ingest inline CSV data into a specified table
- **`kusto_get_shots`** - Retrieve semantically similar query examples from a shots table using AI embeddings

#### Eventstreams - 6 Tools:
- **`list_eventstreams`** - List all Eventstreams in your Fabric workspace
- **`get_eventstream`** - Get detailed information about a specific Eventstream
- **`get_eventstream_definition`** - Retrieve complete JSON definition of an Eventstream

## Getting Started

### Prerequisites
1. Install either the stable or Insiders release of VS Code:
   * [💫 Stable release](https://code.visualstudio.com/download)
   * [🔮 Insiders release](https://code.visualstudio.com/insiders)
2. Install the [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) and [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) extensions
3. Install `uv`  
```ps
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```  
or, check here for [other install options](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)

4. Open VS Code in an empty folder

## 📦 Installation

### 🔧 Install from GitHub (Recommended for Development)  

If you want to use the latest version or contribute to development, you can install directly from the GitHub repository:

#### Quick Setup Steps:

1. **Prerequisites**
   - Python 3.10+ installed and added to PATH
   - `uv` package manager installed (see installation steps above)
   - VS Code with GitHub Copilot extensions

2. **Clone the Repository**
   ```bash
   git clone https://github.com/melisa-l/fabric-rti-mcp.git
   cd fabric-rti-mcp
   ```

3. **Install Dependencies**
   ```bash
   pip install -e .
   ```
   Or using uv:
   ```bash
   uv pip install -e .
   ```

4. **Configure VS Code**
   Add the following to your `settings.json` or `mcp.json` file:
   - Press `Ctrl+Shift+P` and search for "Preferences: Open User Settings (JSON)"
   - Add the MCP server configuration below
   - **Important**: Update the `--directory` path to match where you cloned the repository

   - **Important**: Update the `--directory` path to match where you cloned the repository

   **Example configuration:**
   ```json
   {
       "mcp": {
           "servers": {
               "fabric-rti-mcp": {
                   "command": "uv",
                   "args": [
                       "--directory",
                       "C:/Users/YourUsername/fabric-rti-mcp/",
                       "run",
                       "-m",
                       "fabric_rti_mcp.server"
                   ],
                   "env": {
                       "FABRIC_SQL_ENDPOINT": "your-workspace-name.datawarehouse.fabric.microsoft.com",
                       "FABRIC_LAKEHOUSE_NAME": "YourLakehouseName"
                   }
               }
           }
       }
   }
   ```

5. **Configure Environment Variables**
   - **FABRIC_SQL_ENDPOINT** (Required): SQL endpoint for your Fabric lakehouse
     - Find: Fabric Portal → Lakehouse → SQL endpoint → Copy Server value
     - Format: `your-workspace-name.datawarehouse.fabric.microsoft.com`
   - **FABRIC_LAKEHOUSE_NAME** (Required): Name of your lakehouse database

6. **Restart VS Code**
   - Close and reopen VS Code for the MCP server to be recognized
   - The server will automatically start when you use Copilot in Agent mode

#### Verify Installation:
1. Open GitHub Copilot Chat and switch to Agent mode
2. Type "@workspace /tools" to see available MCP tools
3. You should see tools from fabric-rti-mcp (SQL Lakehouse tools primarily)
4. Try a test query: "What tables are in my lakehouse?"

---

### 🔧 Alternative: Install from PyPI (Pip)
The Fabric RTI MCP Server is also available on [PyPI](https://pypi.org/project/microsoft-fabric-rti-mcp/):

#### From VS Code
1. Open command palette (`Ctrl+Shift+P`) and run `MCP: Add Server`
2. Select "Install from Pip"
3. Enter package name: `microsoft-fabric-rti-mcp`
4. Follow the prompts to configure

The process will add these settings to your `settings.json`:

## 🐛 Debugging the MCP Server locally
Assuming you have python installed and the repo cloned:

### Install locally
```bash
pip install -e ".[dev]"
```

### Configure

Follow the [Manual Install](#🔧-manual-install-install-from-source) instructions.

### Attach the debugger
Use the `Python: Attach` configuration in your `launch.json` to attach to the running server. 
Once VS Code picks up the server and starts it, navigate to its output: 
1. Open command palette (Ctrl+Shift+P) and run the command `MCP: List Servers`
2. Navigate to `fabric-rti-mcp` and select `Show Output`
3. Pick up the process ID (PID) of the server from the output
4. Run the `Python: Attach` configuration in your `launch.json` file, and paste the PID of the server in the prompt
5. The debugger will attach to the server process, and you can start debugging


## 🧪 Test the MCP Server

1. Open GitHub Copilot in VS Code and [switch to Agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)
2. You should see the Fabric RTI MCP Server in the list of tools
3. Try a prompt that tells the agent to use the Eventhouse tools, such as "List my Kusto tables"
4. The agent should be able to use the Fabric RTI MCP Server tools to complete your query


## ⚙️ Configuration

The MCP server can be configured using the following environment variables:

### Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `FABRIC_SQL_ENDPOINT` | Your Fabric SQL endpoint (without https://) | `workspace.datawarehouse.fabric.microsoft.com` |
| `FABRIC_LAKEHOUSE_NAME` | Name of your lakehouse database (case-sensitive) | `MyLakehouse` |

### Optional Environment Variables

| Variable | Service | Description | Default | Example |
|----------|---------|-------------|---------|---------|
| `FABRIC_API_BASE` | Global | Base URL for Microsoft Fabric API | `https://api.fabric.microsoft.com/v1` | `https://api.fabric.microsoft.com/v1` |
| `FABRIC_BASE_URL` | Global | Base URL for Microsoft Fabric web interface | `https://fabric.microsoft.com` | `https://fabric.microsoft.com` |

### Embedding Endpoint Configuration

The `AZ_OPENAI_EMBEDDING_ENDPOINT` is used by the semantic search functionality (e.g., `kusto_get_shots` function) to find similar query examples. 

**Format Requirements:**
```
https://{your-openai-resource}.openai.azure.com/openai/deployments/{deployment-name}/embeddings?api-version={api-version};impersonate
```

**Components:**
- `{your-openai-resource}`: Your Azure OpenAI resource name
- `{deployment-name}`: Your text embedding deployment name (e.g., `text-embedding-ada-002`)
- `{api-version}`: API version (e.g., `2024-10-21`, `2023-05-15`)
- `;impersonate`: Authentication method (you might use managed identity)

**Authentication Requirements:**
- Your Azure identity must have access to the OpenAI resource
- In case using managed identity, the OpenAI resource must should be configured to accept managed identity authentication
- The deployment must exist and be accessible

### Configuration of Shots Table
The `kusto_get_shots` tool retrieves shots that are most similar to your prompt from the shots table. This function requires configuration of:
- **Shots table**: Should have an "EmbeddingText" (string) column containing the natural language prompt, "AugmentedText" (string) column containing the respective KQL, and "EmbeddingVector" (dynamic) column containing the embedding vector of the EmbeddingText.
- **Azure OpenAI embedding endpoint**: Used to create embedding vectors for your prompt. Note that this endpoint must use the same model that was used for creating the "EmbeddingVector" column in the shots table.

## 🔑 Authentication

The MCP Server uses Azure Identity via [`DefaultAzureCredential`](https://learn.microsoft.com/en-us/azure/developer/python/sdk/authentication/credential-chains?tabs=dac) for secure, seamless authentication with **automatic token caching** to avoid repeated authentication prompts.

### Authentication Methods (in priority order):

1. **Environment Variables** (`EnvironmentCredential`) - Perfect for CI/CD pipelines
2. **Managed Identity** (`ManagedIdentityCredential`) - For Azure-hosted deployments
3. **Visual Studio Code** (`VisualStudioCodeCredential`) - Uses your VS Code credentials
4. **Azure CLI** (`AzureCliCredential`) - **⭐ RECOMMENDED** - Uses your existing Azure CLI login
5. **Azure PowerShell** (`AzurePowerShellCredential`) - Uses your Az PowerShell login
6. **Azure Developer CLI** (`AzureDeveloperCliCredential`) - Uses your azd login
7. **Interactive Browser** (`InteractiveBrowserCredential`) - Falls back to browser-based login if needed

### 🎯 Recommended Setup: Azure CLI (No repeated authentication prompts!)

The **Azure CLI method provides the best user experience** with automatic token caching:

#### Install Azure CLI:

**Windows:**
```powershell
winget install Microsoft.AzureCLI
```
Or download from: https://aka.ms/installazurecliwindows

**Mac:**
```bash
brew install azure-cli
```

**Linux:**
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

#### Authenticate Once:
```bash
az login
```

**That's it!** The MCP server will automatically use these cached credentials for all queries. You'll never be prompted to authenticate again (unless the token expires, which is automatically refreshed).

### How Token Caching Works

- **First request**: Authenticates using your preferred method (Azure CLI recommended)
- **Subsequent requests**: Automatically reuses the cached token
- **Token expiration**: Automatically refreshed in the background
- **Zero prompts**: Once authenticated, no more browser pop-ups or sign-in requests!

### Alternative: Browser-Based Authentication

If you don't install Azure CLI, the server will fall back to interactive browser authentication:
- First query opens a browser for sign-in
- Token is cached for the session
- May require occasional re-authentication

**For the smoothest experience, we strongly recommend using Azure CLI!**

## HTTP Mode Configuration for MCP Server

When the MCP server is running locally to the agent in HTTP mode or is deployed to Azure, the following environment variables are used to define and enable HTTP mode. You can find practical examples of this setup in the `tests/live/test_kusto_tools_live_http.py` file:

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `FABRIC_RTI_TRANSPORT` | Transport mode for the server | `stdio` | `http` |
| `FABRIC_RTI_HTTP_HOST` | Host address for HTTP server | `127.0.0.1` | `0.0.0.0` |
| `FABRIC_RTI_HTTP_PORT` | Port for HTTP server | `3000` | `8080` |
| `FABRIC_RTI_HTTP_PATH` | HTTP path for MCP endpoint | `/mcp` | `/mcp` |
| `FABRIC_RTI_STATELESS_HTTP` | Whether to use stateless HTTP mode | `false` | `true` |

HTTP clients connecting to the server need to include the appropriate authentication token in the request headers:

```python
# Example from test_kusto_tools_live_http.py
auth_header = f"Bearer {token.token}"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
    "Authorization": auth_header,
}
```

### OBO Flow Authentication

If your scenario involves a user token with a non-Kusto audience and you need to exchange it for a Kusto audience token using the OBO flow, the Fabric RTI MCP Server  can handle this exchange automatically by setting the following environment variables:

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `USE_OBO_FLOW` | Enable OBO flow for token exchange | `false` | `true` |
| `FABRIC_RTI_MCP_AZURE_TENANT_ID` | `72f988bf-86f1-41af-91ab-2d7cd011db47` (Microsoft) | `72f988bf-86f1-41af-91ab-2d7cd011db47` |
| `FABRIC_RTI_MCP_ENTRA_APP_CLIENT_ID` | Entra App (AAD) Client ID | Your client ID |
| `FABRIC_RTI_MCP_USER_MANAGED_IDENTITY_CLIENT_ID` | User Managed Identity Client ID | Your UMI client ID |

This flow is typically used in OAuth scenarios where a gateway like Azure API Management (APIM) is involved (example: https://github.com/ai-microsoft/adsmcp-apim-dual-validation?tab=readme-ov-file). The user authenticates via Entra ID, and APIM forwards the token to the MCP server. The token audience is not Kusto, so the MCP server must perform an OBO token exchange to get a token with the Kusto audience.
To support this setup, your Microsoft Entra App must be configured to use Federated Credentials following the official guide: https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation. This enables the app to exchange tokens (OBO).
Additionally, the Entra app must be granted Azure Data Explorer API permissions to successfully acquire an OBO token with the Kusto audience.

### Remote Deployment 
The MCP server can be deployed using the method of your choice. For example, you can follow the guide at https://github.com/Azure-Samples/mcp-sdk-functions-hosting-python/blob/main/ExistingServer.md to deploy the MCP server to an Azure Function App.

## 🛡️ Security Note

Your credentials are always handled securely through the official [Azure Identity SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/identity/Azure.Identity/README.md) - **we never store or manage tokens directly**.

MCP as a phenomenon is very novel and cutting-edge. As with all new technology standards, consider doing a security review to ensure any systems that integrate with MCP servers follow all regulations and standards your system is expected to adhere to. This includes not only the Azure MCP Server, but any MCP client/agent that you choose to implement down to the model provider.


## 👥 Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

## 🤝 Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Data Collection

The software may collect information about you and your use of the software and send it to Microsoft. Microsoft may use this information to provide services and improve our products and services. You may turn off the telemetry as described in the repository. There are also some features in the software that may enable you and Microsoft to collect data from users of your applications. If you use these features, you must comply with applicable law, including providing appropriate notices to users of your applications together with a copy of Microsoft’s privacy statement. Our privacy statement is located at https://go.microsoft.com/fwlink/?LinkID=824704. You can learn more about data collection and use in the help documentation and our privacy statement. Your use of the software operates as your consent to these practices.


## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
