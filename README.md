# fabric-lakehouse-mcp[![PyPI](https://img.shields.io/pypi/v/fabric-lakehouse-mcp?style=flat-square)](https://pypi.org/project/fabric-lakehouse-mcp/) [![GitHub](https://img.shields.io/badge/GitHub-fabric--lakehouse--mcp-181717?style=flat-square&logo=github)](https://github.com/melisa-l/fabric-rti-mcp) [![PyPI Downloads](https://static.pepy.tech/badge/fabric-lakehouse-mcp)](https://pepy.tech/projects/fabric-lakehouse-mcp)



[![PyPI](https://img.shields.io/pypi/v/fabric-lakehouse-mcp?style=flat-square)](https://pypi.org/project/fabric-lakehouse-mcp/) [![GitHub](https://img.shields.io/badge/GitHub-fabric--lakehouse--mcp-181717?style=flat-square&logo=github)](https://github.com/melisa-l/fabric-rti-mcp) [![PyPI Downloads](https://static.pepy.tech/badge/fabric-lakehouse-mcp)](https://pepy.tech/projects/fabric-lakehouse-mcp)## 🎯 Overview



## 🎯 OverviewA Model Context Protocol (MCP) server for [Microsoft Fabric Lakehouses](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview). 

This server enables AI agents to query and analyze data in Fabric SQL Lakehouses using natural language through the MCP interface.

A Model Context Protocol (MCP) server for [Microsoft Fabric Lakehouses](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview). 

This server enables AI agents to query and analyze data in Fabric SQL Lakehouses using natural language through the MCP interface.> [!NOTE]  

> This project is in Public Preview and implementation may significantly change prior to General Availability.

> [!NOTE]  

> This project is in Public Preview and implementation may significantly change prior to General Availability.### 📦 Quick Start



### 📦 Quick StartInstall via pip and configure in VS Code:



Install via pip and configure in VS Code:```bash

pip install fabric-lakehouse-mcp

```bash```

pip install fabric-lakehouse-mcp

```See the [Quick Start Guide](QUICKSTART_GUIDE.md) for full setup instructions.



See the [Quick Start Guide](QUICKSTART_GUIDE.md) for full setup instructions.### 🔍 How It Works



### 🔍 How It WorksThe Fabric Lakehouse MCP Server acts as a bridge between AI agents and Microsoft Fabric SQL Lakehouses:



The Fabric Lakehouse MCP Server acts as a bridge between AI agents and Microsoft Fabric SQL Lakehouses:- 🔄 **MCP Protocol**: Uses the Model Context Protocol to expose Lakehouse capabilities as tools

- 🏗️ **Natural Language to SQL**: AI agents can translate natural language requests into SQL queries

- 🔄 **MCP Protocol**: Uses the Model Context Protocol to expose Lakehouse capabilities as tools- 💡 **Secure Authentication**: Uses Azure CLI authentication for secure access

- 🏗️ **Natural Language to SQL**: AI agents can translate natural language requests into SQL queries- ⚡ **Direct SQL Access**: Query Lakehouse tables via the SQL Analytics Endpoint

- 💡 **Secure Authentication**: Uses Azure CLI authentication for secure access

- ⚡ **Direct SQL Access**: Query Lakehouse tables via the SQL Analytics Endpoint### ✨ Supported Services



### ✨ Supported Services**SQL Lakehouse**: Query and analyze data in Microsoft Fabric [Lakehouses](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview) using SQL:

- List all tables in your Lakehouse

**SQL Lakehouse**: Query and analyze data in Microsoft Fabric [Lakehouses](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview) using SQL:- Get detailed schema information for tables

- List all tables in your Lakehouse- View query execution history

- Get detailed schema information for tables

- View query execution history### 🔍 Example Prompts



### 🔍 Example Prompts**Lakehouse Analytics:**

- "What tables are in my lakehouse?"

**Lakehouse Analytics:**- "Show me the schema of the customers table"

- "What tables are in my lakehouse?"- "List all tables and their column types"

- "Show me the schema of the customers table"- "What queries have been run recently?"

- "List all tables and their column types"

- "What queries have been run recently?"### Available Tools



### Available Tools#### SQL Lakehouse - 2 Tools:

- **`sql_list_lakehouse_tables`** - List all tables in a Fabric SQL lakehouse

#### SQL Lakehouse - 2 Tools:- **`sql_get_table_schema`** - Get detailed schema information for a specific table in the lakehouse

- **`sql_list_lakehouse_tables`** - List all tables in a Fabric SQL lakehouse

- **`sql_get_table_schema`** - Get detailed schema information for a specific table in the lakehouse#### Query History - 2 Tools:

- **`query_history_list`** - List recent SQL queries executed on the lakehouse

#### Query History - 2 Tools:- **`query_history_get`** - Get detailed information about a specific query execution

- **`query_history_list`** - List recent SQL queries executed on the lakehouse

- **`query_history_get`** - Get detailed information about a specific query execution## Getting Started



## Getting Started### Prerequisites

1. Install either the stable or Insiders release of VS Code:

### Prerequisites   * [💫 Stable release](https://code.visualstudio.com/download)

1. **Python 3.10+** installed   * [🔮 Insiders release](https://code.visualstudio.com/insiders)

2. **Azure CLI** installed ([Download](https://learn.microsoft.com/cli/azure/install-azure-cli))2. Install the [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) and [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) extensions

3. **VS Code** with GitHub Copilot extensions3. Install `uv`  

4. Access to a **Microsoft Fabric Lakehouse**```ps

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

### Installation```  

or, check here for [other install options](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)

#### Quick Install (PyPI)

```bash4. Open VS Code in an empty folder

pip install fabric-lakehouse-mcp

```## 📦 Installation



#### Development Install (from source)### 🔧 Install from GitHub (Recommended for Development)  

```bash

git clone https://github.com/melisa-l/fabric-rti-mcp.gitIf you want to use the latest version or contribute to development, you can install directly from the GitHub repository:

cd fabric-rti-mcp

pip install -e ".[dev]"#### Quick Setup Steps:

```

1. **Prerequisites**

### Configuration   - Python 3.10+ installed and added to PATH

   - `uv` package manager installed (see installation steps above)

Add to your VS Code MCP settings:   - VS Code with GitHub Copilot extensions



```json2. **Clone the Repository**

{   ```bash

  "mcpServers": {   git clone https://github.com/melisa-l/fabric-rti-mcp.git

    "fabric-lakehouse": {   cd fabric-rti-mcp

      "command": "uvx",   ```

      "args": ["fabric-lakehouse-mcp"],

      "env": {3. **Install Dependencies**

        "FABRIC_SQL_ENDPOINT": "your-workspace-id.datawarehouse.fabric.microsoft.com",   ```bash

        "FABRIC_LAKEHOUSE_NAME": "YourLakehouseName",   pip install -e .

        "UV_LINK_MODE": "copy"   ```

      }   Or using uv:

    }   ```bash

  }   uv pip install -e .

}   ```

```

4. **Configure VS Code**

See the [Quick Start Guide](QUICKSTART_GUIDE.md) for detailed setup instructions.   Add the following to your `settings.json` or `mcp.json` file:

   - Press `Ctrl+Shift+P` and search for "Preferences: Open User Settings (JSON)"

## 🧪 Testing   - Add the MCP server configuration below

   - **Important**: Update the `--directory` path to match where you cloned the repository

1. Open GitHub Copilot in VS Code and switch to Agent mode

2. You should see the Fabric Lakehouse MCP Server in the tools list   - **Important**: Update the `--directory` path to match where you cloned the repository

3. Try prompts like:

   - "List all tables in my lakehouse"   **Example configuration:**

   - "Show me the schema for the customers table"   ```json

   - "What queries have been run recently?"   {

       "mcp": {

## ⚙️ Configuration Reference           "servers": {

               "fabric-rti-mcp": {

### Required Environment Variables                   "command": "uv",

                   "args": [

| Variable | Description | Example |                       "--directory",

|----------|-------------|---------|                       "C:/Users/YourUsername/fabric-rti-mcp/",

| `FABRIC_SQL_ENDPOINT` | Your Fabric SQL endpoint (without https://) | `workspace.datawarehouse.fabric.microsoft.com` |                       "run",

| `FABRIC_LAKEHOUSE_NAME` | Name of your lakehouse database (case-sensitive) | `MyLakehouse` |                       "-m",

                       "fabric_rti_mcp.server"

### Optional Environment Variables                   ],

                   "env": {

| Variable | Description | Default | Example |                       "FABRIC_SQL_ENDPOINT": "your-workspace-name.datawarehouse.fabric.microsoft.com",

|----------|-------------|---------|---------|                       "FABRIC_LAKEHOUSE_NAME": "YourLakehouseName"

| `FABRIC_API_BASE` | Base URL for Microsoft Fabric API | `https://api.fabric.microsoft.com/v1` | Custom API endpoint |                   }

| `FABRIC_BASE_URL` | Base URL for Microsoft Fabric web interface | `https://fabric.microsoft.com` | Custom Fabric URL |               }

| `UV_LINK_MODE` | Set to `copy` to avoid OneDrive hardlink issues | - | `copy` |           }

       }

## 🔑 Authentication   }

   ```

The MCP Server uses Azure Identity via [`DefaultAzureCredential`](https://learn.microsoft.com/en-us/azure/developer/python/sdk/authentication/credential-chains?tabs=dac) for secure authentication with **automatic token caching**.

5. **Configure Environment Variables**

### 🎯 Recommended: Azure CLI Authentication   - **FABRIC_SQL_ENDPOINT** (Required): SQL endpoint for your Fabric lakehouse

     - Find: Fabric Portal → Lakehouse → SQL endpoint → Copy Server value

**Install Azure CLI:**     - Format: `your-workspace-name.datawarehouse.fabric.microsoft.com`

   - **FABRIC_LAKEHOUSE_NAME** (Required): Name of your lakehouse database

**Windows:**

```powershell6. **Restart VS Code**

winget install Microsoft.AzureCLI   - Close and reopen VS Code for the MCP server to be recognized

```   - The server will automatically start when you use Copilot in Agent mode



**macOS:**#### Verify Installation:

```bash1. Open GitHub Copilot Chat and switch to Agent mode

brew install azure-cli2. Type "@workspace /tools" to see available MCP tools

```3. You should see tools from fabric-rti-mcp (SQL Lakehouse tools primarily)

4. Try a test query: "What tables are in my lakehouse?"

**Linux:**

```bash---

curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

```### 🔧 Alternative: Install from PyPI (Pip)

The Fabric RTI MCP Server is also available on [PyPI](https://pypi.org/project/microsoft-fabric-rti-mcp/):

**Authenticate:**

```bash## Getting Started

az login

```### Prerequisites

1. **Python 3.10+** installed

That's it! The MCP server will automatically use these cached credentials.2. **Azure CLI** installed ([Download](https://learn.microsoft.com/cli/azure/install-azure-cli))

3. **VS Code** with GitHub Copilot extensions

### Alternative Authentication Methods4. Access to a **Microsoft Fabric Lakehouse**



`DefaultAzureCredential` tries these methods in order:### Installation

1. Environment Variables

2. Managed Identity (for Azure deployments)#### Quick Install (PyPI)

3. Visual Studio Code credentials```bash

4. **Azure CLI** (recommended)pip install fabric-lakehouse-mcp

5. Azure PowerShell```

6. Interactive Browser (fallback)

#### Development Install (from source)

## 🐛 Debugging```bash

git clone https://github.com/melisa-l/fabric-rti-mcp.git

### Local Developmentcd fabric-rti-mcp

pip install -e ".[dev]"

1. Install with dev dependencies:```

```bash

pip install -e ".[dev]"### Configuration

```

Add to your VS Code MCP settings:

2. Configure your environment variables (see Configuration section)

```json

3. Attach debugger:{

   - Open VS Code Command Palette (`Ctrl+Shift+P`)  "mcpServers": {

   - Run `MCP: List Servers`    "fabric-lakehouse": {

   - Select `fabric-lakehouse` and click `Show Output`      "command": "uvx",

   - Note the PID from the output      "args": ["fabric-lakehouse-mcp"],

   - Use VS Code's `Python: Attach` debug configuration with that PID      "env": {

        "FABRIC_SQL_ENDPOINT": "your-workspace-id.datawarehouse.fabric.microsoft.com",

## 🛡️ Security Note        "FABRIC_LAKEHOUSE_NAME": "YourLakehouseName",

        "UV_LINK_MODE": "copy"

Your credentials are handled securely through the official [Azure Identity SDK](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/identity/Azure.Identity/README.md) - **we never store or manage tokens directly**.      }

    }

## 👥 Contributing  }

}

This project welcomes contributions and suggestions. Most contributions require you to agree to a```

Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us

the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.See the [Quick Start Guide](QUICKSTART_GUIDE.md) for detailed setup instructions.



When you submit a pull request, a CLA bot will automatically determine whether you need to provide## 🧪 Testing

a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions

provided by the bot. You will only need to do this once across all repos using our CLA.1. Open GitHub Copilot in VS Code and switch to Agent mode

2. You should see the Fabric Lakehouse MCP Server in the tools list

## 🤝 Code of Conduct3. Try prompts like:

   - "List all tables in my lakehouse"

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).   - "Show me the schema for the customers table"

For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or   - "What queries have been run recently?"

contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## ⚙️ Configuration Reference

## 📊 Data Collection

### Required Environment Variables

The software may collect information about you and your use of the software and send it to Microsoft. Microsoft may use this information to provide services and improve our products and services. You may turn off the telemetry as described in the repository. There are also some features in the software that may enable you and Microsoft to collect data from users of your applications. If you use these features, you must comply with applicable law, including providing appropriate notices to users of your applications together with a copy of Microsoft's privacy statement. Our privacy statement is located at https://go.microsoft.com/fwlink/?LinkID=824704. You can learn more about data collection and use in the help documentation and our privacy statement. Your use of the software operates as your consent to these practices.

| Variable | Description | Example |

## ™️ Trademarks|----------|-------------|---------|

| `FABRIC_SQL_ENDPOINT` | Your Fabric SQL endpoint (without https://) | `workspace.datawarehouse.fabric.microsoft.com` |

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft | `FABRIC_LAKEHOUSE_NAME` | Name of your lakehouse database (case-sensitive) | `MyLakehouse` |

trademarks or logos is subject to and must follow 

[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).### Optional Environment Variables

Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.

Any use of third-party trademarks or logos are subject to those third-party's policies.| Variable | Description | Default | Example |

|----------|-------------|---------|---------|
| `FABRIC_API_BASE` | Base URL for Microsoft Fabric API | `https://api.fabric.microsoft.com/v1` | Custom API endpoint |
| `FABRIC_BASE_URL` | Base URL for Microsoft Fabric web interface | `https://fabric.microsoft.com` | Custom Fabric URL |
| `UV_LINK_MODE` | Set to `copy` to avoid OneDrive hardlink issues | - | `copy` |

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
