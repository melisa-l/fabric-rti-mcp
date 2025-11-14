# 🚀 Quick Start Guide - Fabric Lakehouse MCP Server

Get up and running with the Fabric Lakehouse MCP Server in **10 minutes**!

This guide uses VS Code's built-in MCP configuration system with `mcp.json`.

---

## 📋 What You'll Need

1. **VS Code** ([Download](https://code.visualstudio.com/))
2. **GitHub Copilot** subscription (required for MCP)
3. **Microsoft Fabric** workspace with a Lakehouse
4. **Access** to your Fabric Lakehouse SQL endpoint

---

## 📖 Overview

We'll set up the MCP server using VS Code's command palette, which will:
1. Install the package from PyPI
2. Create/update your `mcp.json` configuration
3. Set up your Fabric connection details

**No manual JSON editing required!**

---

# Step 1: Install Prerequisites

## 1.1 Install Python

1. Download Python 3.10+ from [python.org](https://www.python.org/downloads/)
2. **Important:** Check "Add Python to PATH" during installation
3. Verify installation:
   ```powershell
   python --version
   ```
   Should show: `Python 3.10.0` or higher

## 1.2 Install Azure CLI (Recommended)

**Why?** Azure CLI provides seamless authentication without browser prompts.

### Windows
Download and install from: [Azure CLI for Windows](https://aka.ms/installazurecliwindows)

Or via PowerShell:
```powershell
winget install Microsoft.AzureCLI
```

### Mac
```bash
brew install azure-cli
```

### Linux
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

**Verify installation:**
```powershell
az --version
```

### Authenticate with Azure CLI

Run this command once to authenticate:
```powershell
az login
```

This will:
1. Open your browser
2. Ask you to sign in with your Microsoft account
3. Cache your credentials locally

**You only need to do this once!** The MCP server will automatically use these cached credentials for all future queries without prompting you again.

## 1.3 Install uv Package Manager (Optional)

Open PowerShell and run:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Close and reopen PowerShell**, then verify:
```powershell
uv --version
```

## 1.4 Install VS Code Extensions

1. Open VS Code
2. Press `Ctrl+Shift+X` (Extensions)
3. Install these two extensions:
   - **GitHub Copilot**
   - **GitHub Copilot Chat**

---

# Step 2: Get Fabric Connection Details

You need TWO pieces of information from Fabric Portal.

## 2.1 Get SQL Endpoint

1. Go to [Fabric Portal](https://app.fabric.microsoft.com/)
2. Navigate to your **Workspace**
3. Open your **Lakehouse**
4. Click **"SQL endpoint"** button in the top ribbon
5. Copy the **Server** value

**Example:** `abc123-workspace.datawarehouse.fabric.microsoft.com`

📝 **Write this down** - you'll need it in Step 3!

## 2.2 Get Lakehouse Name

1. Still in Fabric Portal, note your Lakehouse name
2. It's shown in the title bar/breadcrumb
3. **Must be exact** (case-sensitive)

**Example:** `SalesLakehouse` or `MyLakehouse`

📝 **Write this down** - you'll need it in Step 3!

---

# Step 3: Add MCP Server in VS Code

Now we'll configure the MCP server using VS Code's built-in command.

## 3.1 Open Command Palette

1. Open VS Code
2. Press **`Ctrl+Shift+P`** (Windows/Linux) or **`Cmd+Shift+P`** (Mac)
3. Type: **`MCP: Add Server`**
4. Press **Enter**

## 3.2 Select "pip (Python)"

You'll see installation method options:
- npm (Node.js)
- **pip (Python)** ← **Select this**
- uvx (Python via uv)
- docker
- Other

**Click on "pip (Python)"**

## 3.3 Enter Package Name

VS Code prompts: **"Enter the package name:"**

Type: **`fabric-lakehouse-mcp`**

Press **Enter**

## 3.4 Add Environment Variables

Now VS Code will ask for environment variables. You need to add TWO.

### Variable 1: FABRIC_SQL_ENDPOINT

**Prompt:** "Enter environment variable name (or press Enter to skip):"

1. Type: **`FABRIC_SQL_ENDPOINT`**
2. Press **Enter**

**Prompt:** "Enter value for FABRIC_SQL_ENDPOINT:"

1. Paste your SQL endpoint from Step 2.1
   - Example: `abc123-workspace.datawarehouse.fabric.microsoft.com`
   - ⚠️ **No** `https://`
   - ⚠️ **No** port number
   - Just the hostname
2. Press **Enter**

### Variable 2: FABRIC_LAKEHOUSE_NAME

**Prompt:** "Enter environment variable name (or press Enter to skip):"

1. Type: **`FABRIC_LAKEHOUSE_NAME`**
2. Press **Enter**

**Prompt:** "Enter value for FABRIC_LAKEHOUSE_NAME:"

1. Type your lakehouse name from Step 2.2
   - Example: `SalesLakehouse`
   - Must match exactly (case-sensitive)
2. Press **Enter**

### Finish Setup

**Prompt:** "Enter environment variable name (or press Enter to skip):"

Press **Enter** (we're done adding variables)

VS Code will now:
- ✅ Create/update your `mcp.json` file
- ✅ Install `fabric-lakehouse-mcp` package
- ✅ Register the MCP server

---

# Step 4: Verify Configuration

## 4.1 Check MCP Server List

1. Press `Ctrl+Shift+P`
2. Type: **`MCP: List Servers`**
3. Press Enter

You should see **`fabric-lakehouse-mcp`** in the list!

## 4.2 View Configuration

Your `mcp.json` file was created at:

- **Windows:** `%APPDATA%\Code\User\globalStorage\mcp.json`
- **Mac:** `~/Library/Application Support/Code/User/globalStorage/mcp.json`  
- **Linux:** `~/.config/Code/User/globalStorage/mcp.json`

It should look like this:

```json
{
    "mcpServers": {
        "fabric-lakehouse-mcp": {
            "command": "python",
            "args": ["-m", "fabric_rti_mcp.server"],
            "env": {
                "FABRIC_SQL_ENDPOINT": "abc123-workspace.datawarehouse.fabric.microsoft.com",
                "FABRIC_LAKEHOUSE_NAME": "SalesLakehouse"
            }
        }
    }
}
```

## 4.3 Restart VS Code

**Important:** Close and reopen VS Code for changes to take effect.

---

# Step 5: Test It! 🎉

## 5.1 Open Copilot Chat

Press **`Ctrl+Alt+I`** (or click the chat icon in the sidebar)

## 5.2 Check Available Tools

In the chat, type:
```
@workspace /tools
```

You should see tools from `fabric-lakehouse-mcp`:
- `lakehouse_sql_query`
- `lakehouse_list_tables`
- `lakehouse_describe_table`
- And more...

## 5.3 Run Your First Query

Type in the chat:
```
What tables are in my lakehouse?
```

**What happens:**

### If you installed Azure CLI and ran `az login`:
1. Copilot will use the `lakehouse_list_tables` tool
2. Authentication happens automatically using cached Azure CLI credentials
3. **No browser prompts!** 🎉
4. You'll see your lakehouse tables listed immediately

### If you didn't install Azure CLI:
1. Copilot will use the `lakehouse_list_tables` tool
2. A browser window pops up for authentication (first time only)
3. Sign in with your Microsoft account
4. Credentials are cached, so you won't be prompted again in this session
5. You'll see your lakehouse tables listed!

**If you see your tables, you're all set!** ✅

> **💡 Pro Tip:** Using Azure CLI (`az login`) provides the smoothest experience with zero authentication prompts after initial setup!

---

# 🎯 Example Queries to Try

Now that you're connected, try these prompts:

```
Show me the schema of the Customer table
```

```
Give me 5 sample rows from the Sales table
```

```
How many tables do I have in my lakehouse?
```

```
Find all tables that have a CustomerID column
```

```
What's the data type of the CreatedDate column in the Orders table?
```

```
Find relationships between tables in my lakehouse
```

---

# 🆘 Troubleshooting

## Problem: "MCP server not found in list"

**Solution:**
1. Make sure you selected "pip (Python)" not another method
2. Check that package name was exactly: `fabric-lakehouse-mcp`
3. Try running the "MCP: Add Server" command again
4. Restart VS Code

## Problem: "No tools showing in chat"

**Solution:**
1. Make sure you typed `@workspace /tools` exactly
2. Restart VS Code completely (close all windows)
3. Check `Ctrl+Shift+P` → "MCP: List Servers" shows your server
4. Look for errors: `Ctrl+Shift+P` → "MCP: List Servers" → click your server → "Show Output"

## Problem: "Authentication window doesn't appear"

**Solution:**
1. Check your browser isn't blocking pop-ups
2. Try the query again
3. Make sure you're logged into [Fabric Portal](https://app.fabric.microsoft.com/)
4. Verify your Fabric workspace permissions

## Problem: "Getting prompted to authenticate repeatedly"

**This is now fixed!** The latest version uses cached authentication tokens.

**For the best experience:**
1. Install Azure CLI (see Step 1.2)
2. Run `az login` in PowerShell/Terminal
3. Restart VS Code
4. You'll never be prompted again!

**Alternative solutions if still having issues:**
1. Make sure you're on the latest version:
   ```powershell
   pip install --upgrade fabric-lakehouse-mcp
   ```
2. Restart VS Code completely after upgrading
3. If using VS Code's built-in terminal, make sure it's authenticated:
   - Open PowerShell/Terminal
   - Run `az login`
   - Close and reopen VS Code

**How it works:**
- The MCP server uses `DefaultAzureCredential` which automatically finds and caches your credentials
- First priority: Azure CLI credentials (from `az login`)
- Credentials are cached and automatically refreshed
- No browser prompts after initial authentication!

## Problem: "No tables found" or empty results

**Solution:**
1. Double-check your `FABRIC_SQL_ENDPOINT`:
   - Should end with `.datawarehouse.fabric.microsoft.com`
   - No `https://` prefix
   - No port numbers (like `:1433`)
2. Verify `FABRIC_LAKEHOUSE_NAME` is exact (case-sensitive)
3. Make sure your lakehouse actually has tables
4. Check Fabric workspace access permissions

## Problem: "Python not found"

**Solution:**
1. Verify Python installed: `python --version` in PowerShell
2. If not found, reinstall Python with "Add to PATH" checked
3. Close and reopen PowerShell/VS Code after installing
4. Try `py --version` (Windows alternative command)

## Problem: Need to change connection details

**Solution:**

### Option 1: Re-run Setup
1. `Ctrl+Shift+P` → "MCP: Remove Server"
2. Select `fabric-lakehouse-mcp`
3. Run "MCP: Add Server" again with correct details

### Option 2: Edit mcp.json Directly
1. Find your `mcp.json` file:
   - Windows: `%APPDATA%\Code\User\globalStorage\mcp.json`
   - Mac: `~/Library/Application Support/Code/User/globalStorage/mcp.json`
2. Edit the `env` section with correct values
3. Save and restart VS Code

---

# 📚 What's Next?

## Explore More Features

- Check out all [available tools](README.md#available-tools) in the README
- Learn about [query history tracking](README.md)
- See [advanced configuration](README.md#️-configuration) options

## Get Help

- **Issues?** [Open a GitHub issue](https://github.com/melisa-l/fabric-rti-mcp/issues)
- **Questions?** Check the [full README](README.md)
- **Contributing?** See [CONTRIB.md](CONTRIB.md)

---

# ✅ Quick Reference

## Your mcp.json Template

If you need to manually edit or recreate your configuration:

**Location:**
- Windows: `%APPDATA%\Code\User\globalStorage\mcp.json`
- Mac: `~/Library/Application Support/Code/User/globalStorage/mcp.json`
- Linux: `~/.config/Code/User/globalStorage/mcp.json`

**Content:**
```json
{
    "mcpServers": {
        "fabric-lakehouse-mcp": {
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

## Essential Commands

| Task | Command |
|------|---------|
| Check Python | `python --version` |
| Check uv | `uv --version` |
| Add MCP server | `Ctrl+Shift+P` → "MCP: Add Server" |
| List MCP servers | `Ctrl+Shift+P` → "MCP: List Servers" |
| Remove MCP server | `Ctrl+Shift+P` → "MCP: Remove Server" |
| Open Copilot Chat | `Ctrl+Alt+I` |
| Check MCP tools | Type `@workspace /tools` in chat |
| View MCP logs | List Servers → Select server → "Show Output" |

---

**Happy querying!** 🚀

Need help? [Open an issue](https://github.com/melisa-l/fabric-rti-mcp/issues) on GitHub.
