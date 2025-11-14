# 🚀 Quick Start Guide - Fabric Lakehouse MCP Server

Get up and running with the Fabric Lakehouse MCP Server in **10 minutes**!

This guide will help you install and configure the MCP server so you can use AI agents to query your Microsoft Fabric Lakehouse with natural language.

---

## 📋 What You'll Need

Before starting, make sure you have:

1. **VS Code** installed ([Download here](https://code.visualstudio.com/))
2. **GitHub Copilot** subscription (required for MCP support)
3. **Microsoft Fabric** workspace with a Lakehouse
4. **Access** to your Fabric Lakehouse SQL endpoint

---

## 🎯 Installation Overview

We'll be using VS Code's built-in MCP configuration system. The setup involves:
1. Installing prerequisites (Python, uv)
2. Getting your Fabric connection details
3. Adding the MCP server through VS Code's command palette
4. Testing the connection

**No manual JSON editing required!** VS Code will create the `mcp.json` file for you.

---

# Step-by-Step Installation

## Step 1: Install Prerequisites

### 1.1 Install Python
- Download Python 3.10 or higher from [python.org](https://www.python.org/downloads/)
- **Important:** During installation, check "Add Python to PATH"
- Verify installation:
  ```powershell
  python --version
  ```
  You should see something like `Python 3.12.0`

### 1.2 Install `uv` Package Manager
Open PowerShell and run:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**After installation, close and reopen PowerShell** to refresh your PATH.

Verify:
```powershell
uv --version
```

### 1.3 Install VS Code Extensions
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search and install:
   - **GitHub Copilot** ([Install](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot))
   - **GitHub Copilot Chat** ([Install](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat))

---

## Step 2: Get Your Fabric Lakehouse Connection Details

You need two pieces of information from your Microsoft Fabric workspace:

### 2.1 Get SQL Endpoint
1. Go to [Fabric Portal](https://app.fabric.microsoft.com/)
2. Navigate to your Workspace
3. Open your **Lakehouse**
4. Click **"SQL endpoint"** in the top ribbon (switches to SQL view)
5. Copy the **Server** value
   - It looks like: `xxxxx-xxxx.datawarehouse.fabric.microsoft.com`
   - **Save this!** You'll need it in Step 3

### 2.2 Get Lakehouse Name
1. Still in Fabric Portal, look at your Lakehouse
2. The name is shown in the title bar / breadcrumb
3. Note the exact name (case-sensitive)
   - Example: `MyLakehouse` or `SalesData`
   - **Save this!** You'll need it in Step 3

---

## Step 3: Configure VS Code

### 3.1 Add MCP Server Using VS Code Command

The easiest way:

1. Open VS Code
2. Press **`Ctrl+Shift+P`** to open Command Palette
3. Type: **"MCP: Add Server"**
4. Select **"Install from Pip"**
5. Enter package name: **`fabric-lakehouse-mcp`**
6. When prompted for environment variables, add your connection details

### 3.2 Manual Configuration (Alternative)

If you prefer to configure manually, create/edit the MCP configuration file:

**Windows:** `%APPDATA%\Code\User\globalStorage\mcp.json`  
**Mac/Linux:** `~/.config/Code/User/globalStorage/mcp.json`

**Copy and paste this entire block** into your `mcp.json`:

**Copy and paste this entire block** into your `mcp.json`:

```json
{
    "mcpServers": {
        "fabric-lakehouse": {
            "command": "uvx",
            "args": [
                "fabric-lakehouse-mcp"
            ],
            "env": {
                "FABRIC_SQL_ENDPOINT": "YOUR-WORKSPACE.datawarehouse.fabric.microsoft.com",
                "FABRIC_LAKEHOUSE_NAME": "YourLakehouseName"
            }
        }
    }
}
```

> **Note:** The MCP configuration should be in `mcp.json`, NOT in `settings.json`. VS Code will warn you if you try to add it to `settings.json`.

### 3.3 Update With Your Information

Replace these two values with what you saved in Step 2:

1. **`FABRIC_SQL_ENDPOINT`**: Replace `YOUR-WORKSPACE.datawarehouse.fabric.microsoft.com` with your actual SQL endpoint
2. **`FABRIC_LAKEHOUSE_NAME`**: Replace `YourLakehouseName` with your actual lakehouse name

**Example:**
```json
"env": {
    "FABRIC_SQL_ENDPOINT": "abc123-workspace.datawarehouse.fabric.microsoft.com",
    "FABRIC_LAKEHOUSE_NAME": "SalesLakehouse"
}
```

### 3.4 Save and Restart

1. **Save** the file (Ctrl+S)
2. **Close VS Code completely**
3. **Reopen VS Code**

---

## Step 4: Verify Installation

### 4.1 Open Copilot Chat
- Press **`Ctrl+Alt+I`** to open Copilot Chat
- Or click the chat icon in the sidebar

### 4.2 Enable Agent Mode
- In the chat input, click the **agent mode icon** (or type `/`)
- This enables MCP tool usage

### 4.3 Check Available Tools
Type this in chat:
```
@workspace /tools
```

You should see tools from `fabric-lakehouse-mcp`, including:
- `lakehouse_sql_query`
- `lakehouse_list_tables`
- `lakehouse_describe_table`
- And more...

### 4.4 Test Your Connection

Try this prompt:
```
What tables are in my lakehouse?
```

**Expected Result:**
- Copilot will use the `lakehouse_list_tables` tool
- You'll see a browser window pop up asking you to authenticate with Microsoft
- After authentication, you'll see a list of your tables

**If this works, you're all set!** 🎉

---

# Option B: Developer Install from GitHub

# Option B: Developer Install from GitHub

For developers who want the latest features or to contribute to the project.

## Step 1: Install Prerequisites

Same as Option A, plus:

### 1.4 Install Git
- Download from [git-scm.com](https://git-scm.com/downloads)
- Verify: `git --version`

---

## Step 2: Clone and Install

### 2.1 Clone the Repository
Open PowerShell or Terminal and run:
```bash
git clone https://github.com/melisa-l/fabric-rti-mcp.git
cd fabric-rti-mcp
```

### 2.2 Install Dependencies
```bash
pip install -e .
```

This installs the package in "editable" mode, meaning changes you make to the code are immediately reflected.

---

## Step 3: Get Your Fabric Lakehouse Connection Details

Same as Option A - Step 2 above.

---

## Step 4: Configure VS Code

### 4.1 Configure MCP Server

Create/edit your MCP configuration file:

**Windows:** `%APPDATA%\Code\User\globalStorage\mcp.json`  
**Mac/Linux:** `~/.config/Code/User/globalStorage/mcp.json`

**Add this configuration:**

```json
{
    "mcpServers": {
        "fabric-lakehouse": {
            "command": "uv",
            "args": [
                "--directory",
                "C:/Users/YourUsername/fabric-rti-mcp/",
                "run",
                "-m",
                "fabric_rti_mcp.server"
            ],
            "env": {
                "FABRIC_SQL_ENDPOINT": "YOUR-WORKSPACE.datawarehouse.fabric.microsoft.com",
                "FABRIC_LAKEHOUSE_NAME": "YourLakehouseName"
            }
        }
    }
}
```

### 4.2 Update Configuration

1. **Update the directory path**: Change `C:/Users/YourUsername/fabric-rti-mcp/` to where you cloned the repo
   - Use **forward slashes** (`/`) even on Windows
   - End with a trailing slash `/`
   - Example: `C:/dev/fabric-rti-mcp/`

2. **Update connection details**: Same as Option A - replace `FABRIC_SQL_ENDPOINT` and `FABRIC_LAKEHOUSE_NAME`

### 4.3 Save and Restart

1. Save the file
2. Close and reopen VS Code

---

## Step 5: Verify Installation

Same as Option A - Step 4 above.

---

# 🎯 Example Queries to Try

Once you're set up, try these prompts in Copilot Chat:

### Basic Exploration
```
What tables exist in my lakehouse?
```

```
Show me the schema of the Customer table
```

```
How many tables do I have?
```

### Data Analysis
```
Show me 5 sample rows from the Sales table
```

```
What columns are in the Product table?
```

```
Find relationships between tables in my lakehouse
```

### Advanced Queries
```
Query the Sales table and show me total revenue by month
```

```
Find all tables that have a column named "CustomerID"
```

```
What's the data type of the "CreatedDate" column in Orders table?
```

---

# 🆘 Troubleshooting

## Problem: MCP Server Not Showing in Tools

**Solution:**
1. Make sure you **restarted VS Code** after configuration
2. Check `settings.json` for syntax errors (missing commas, brackets)
3. Verify the MCP setting is enabled:
   ```json
   "github.copilot.chat.mcp.enabled": true
   ```
4. Check MCP server status:
   - Press `Ctrl+Shift+P`
   - Type "MCP: List Servers"
   - Look for `fabric-lakehouse` in the list

## Problem: "Command 'uvx' not found"

**Solution:**
1. Close and reopen PowerShell/Terminal
2. Verify `uv` is installed: `uv --version`
3. If not installed, run the installation command again:
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

## Problem: Authentication Pop-up Not Appearing

**Solution:**
1. Check your Fabric workspace permissions
2. Make sure you're logged into Microsoft/Azure
3. Try running the query again
4. Check if pop-ups are blocked in your browser

## Problem: "No tables found" or Empty Results

**Solution:**
1. Verify your `FABRIC_SQL_ENDPOINT` is correct:
   - Should end with `.datawarehouse.fabric.microsoft.com`
   - No `https://` prefix
   - No port numbers
2. Verify your `FABRIC_LAKEHOUSE_NAME` matches exactly (case-sensitive)
3. Make sure your lakehouse has tables with data
4. Check Fabric workspace permissions

## Problem: Python Not Found

**Solution:**
1. Verify Python is installed: `python --version`
2. If not found, reinstall Python and **check "Add to PATH"**
3. After installation, close and reopen PowerShell
4. Try again: `python --version`

## Still Having Issues?

1. **Check MCP Server Logs:**
   - Press `Ctrl+Shift+P`
   - Type "MCP: List Servers"
   - Click on `fabric-lakehouse`
   - Click "Show Output"
   - Look for error messages

2. **Verify Configuration:**
   - Make sure `settings.json` is valid JSON (no syntax errors)
   - Use a JSON validator if needed
   - Check that all quotes and brackets match

3. **Test Python Installation:**
   ```powershell
   python -c "import pyodbc; print('pyodbc OK')"
   ```
   If this fails, reinstall the package: `pip install fabric-lakehouse-mcp`

4. **Get Help:**
   - Open an issue on [GitHub](https://github.com/melisa-l/fabric-rti-mcp/issues)
   - Include:
     - Your OS (Windows/Mac/Linux)
     - Python version
     - Error messages from MCP logs
     - Your `settings.json` configuration (remove sensitive info)

---

# 📚 Next Steps

### Learn More
- Read the [full README](README.md) for advanced features
- Explore all [available tools](README.md#available-tools)
- Check out [configuration options](README.md#️-configuration)

### Optional: Add Eventhouse (KQL) Support

If you also want to query Eventhouse with KQL, add these to your `env` section:

```json
"env": {
    "FABRIC_SQL_ENDPOINT": "workspace.datawarehouse.fabric.microsoft.com",
    "FABRIC_LAKEHOUSE_NAME": "MyLakehouse"
}
```

### Contribute
- Read [CONTRIB.md](CONTRIB.md) for contribution guidelines
- Check out [open issues](https://github.com/melisa-l/fabric-rti-mcp/issues)
- Submit bug reports or feature requests

---

# ✅ Quick Reference

## Your Settings Template (Copy & Paste)

> **Important:** Use `mcp.json`, NOT `settings.json`!  
> Location: `%APPDATA%\Code\User\globalStorage\mcp.json` (Windows) or `~/.config/Code/User/globalStorage/mcp.json` (Mac/Linux)

**For PyPI Install:**
```json
{
    "mcpServers": {
        "fabric-lakehouse": {
            "command": "uvx",
            "args": ["fabric-lakehouse-mcp"],
            "env": {
                "FABRIC_SQL_ENDPOINT": "your-endpoint.datawarehouse.fabric.microsoft.com",
                "FABRIC_LAKEHOUSE_NAME": "YourLakehouse"
            }
        }
    }
}
```

**For GitHub Clone:**
```json
{
    "mcpServers": {
        "fabric-lakehouse": {
            "command": "uv",
            "args": [
                "--directory",
                "C:/path/to/fabric-rti-mcp/",
                "run",
                "-m",
                "fabric_rti_mcp.server"
            ],
            "env": {
                "FABRIC_SQL_ENDPOINT": "your-endpoint.datawarehouse.fabric.microsoft.com",
                "FABRIC_LAKEHOUSE_NAME": "YourLakehouse"
            }
        }
    }
}
```

## Essential Commands

| Task | Command |
|------|---------|
| Check Python version | `python --version` |
| Check uv installation | `uv --version` |
| Install from PyPI | `pip install fabric-lakehouse-mcp` |
| Clone from GitHub | `git clone https://github.com/melisa-l/fabric-rti-mcp.git` |
| Edit MCP config | Create/edit `%APPDATA%\Code\User\globalStorage\mcp.json` |
| Add MCP server | `Ctrl+Shift+P` → "MCP: Add Server" |
| Open Copilot Chat | `Ctrl+Alt+I` |
| Check MCP tools | `@workspace /tools` in chat |
| View MCP logs | `Ctrl+Shift+P` → "MCP: List Servers" → "Show Output" |

---

**Happy querying!** 🚀

Need help? [Open an issue](https://github.com/melisa-l/fabric-rti-mcp/issues) on GitHub.
