# 🚀 Quick Start Guide - Fabric RTI MCP Server

Get up and running with the Fabric RTI MCP Server in 5 minutes!

## Prerequisites Checklist

- [ ] Python 3.10 or higher installed
- [ ] VS Code with GitHub Copilot installed
- [ ] `uv` package manager installed
- [ ] Git installed

### Install Prerequisites

**Install Python:**
- Windows: Download from [python.org](https://www.python.org/downloads/)
- Verify: `python --version`

**Install uv (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Install VS Code Extensions:**
1. [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
2. [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)

---

## 3-Step Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/melisa-l/fabric-rti-mcp.git
cd fabric-rti-mcp
```

### Step 2: Install Dependencies
```bash
pip install -e .
```

### Step 3: Configure VS Code

1. **Open Settings JSON:**
   - Press `Ctrl+Shift+P`
   - Type "Preferences: Open User Settings (JSON)"
   - Press Enter

2. **Add MCP Configuration:**
   Copy and paste this configuration, **replacing the path** with your actual repository location:

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
                       "KUSTO_SERVICE_URI": "https://help.kusto.windows.net/",
                       "KUSTO_SERVICE_DEFAULT_DB": "Samples"
                   }
               }
           }
       }
   }
   ```

3. **Update the Path:**
   - Change `C:/Users/YourUsername/fabric-rti-mcp/` to your actual clone location
   - Use forward slashes `/` even on Windows
   - Make sure the path ends with a trailing slash `/`

4. **Save and Restart VS Code**

---

## ✅ Verify Installation

1. **Open Copilot Chat** (Ctrl+Alt+I)
2. **Switch to Agent Mode** (click the icon or type `/`)
3. **Check Available Tools:**
   ```
   @workspace /tools
   ```
   You should see tools from `fabric-rti-mcp`

4. **Test a Query:**
   ```
   List my Kusto databases
   ```

If you see the tools and can execute queries, you're all set! 🎉

---

## 🔧 Optional Configuration

### Add Your Own Fabric Resources

Update the `env` section in your settings.json:

```json
"env": {
    "KUSTO_SERVICE_URI": "https://your-cluster.kusto.windows.net/",
    "KUSTO_SERVICE_DEFAULT_DB": "YourDatabase",
    "FABRIC_SQL_ENDPOINT": "your-lakehouse.datawarehouse.fabric.microsoft.com",
    "FABRIC_LAKEHOUSE_NAME": "YourLakehouseName"
}
```

**Where to find these values:**
- **KUSTO_SERVICE_URI**: Fabric Portal → Eventhouse → Copy cluster URI
- **KUSTO_SERVICE_DEFAULT_DB**: Your default database name in Eventhouse
- **FABRIC_SQL_ENDPOINT**: Fabric Portal → Lakehouse → SQL endpoint
- **FABRIC_LAKEHOUSE_NAME**: Your lakehouse name

---

## 🎯 Example Queries to Try

**Eventhouse (KQL):**
- "Show me sample data from StormEvents table"
- "What databases are available in my Eventhouse?"
- "Analyze storm patterns over the past decade"

**SQL Lakehouse:**
- "What tables exist in my lakehouse?"
- "Describe the schema of table 'Sales'"
- "Find relationships between tables"

**Eventstreams:**
- "List all Eventstreams in my workspace"
- "Show details of my IoT Eventstream"

---

## 🆘 Troubleshooting

### MCP Server Not Showing in Tools
1. Make sure you restarted VS Code after configuration
2. Check the path in settings.json is correct
3. Verify `pip install -e .` completed without errors

### Authentication Issues
- When prompted, sign in with your Microsoft/Azure credentials
- Make sure you have access to the Fabric workspace

### Python/Module Not Found
- Verify Python is in your PATH: `python --version`
- Reinstall dependencies: `pip install -e .`

### Still Having Issues?
- Check the [full README](README.md) for detailed documentation
- Review MCP server logs: `Ctrl+Shift+P` → "MCP: List Servers" → "Show Output"
- Open an issue on [GitHub](https://github.com/melisa-l/fabric-rti-mcp/issues)

---

## 📚 Next Steps

- Explore all [available tools](README.md#available-tools)
- Learn about [debugging](README.md#-debugging-the-mcp-server-locally)
- Check [configuration options](README.md#️-configuration)
- Read about [contributing](CONTRIB.md)

Happy querying! 🚀
