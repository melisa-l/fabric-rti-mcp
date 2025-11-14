# Release History

## 0.3.8 (Upcoming)
### Documentation
- Simplified documentation structure: one README, one quickstart guide, one MCP template
- Removed duplicate and confusing documentation files
- Fixed mcp-manifest.json command name to match actual pip-installed executable

## 0.3.7 (2025-01-14)
### Breaking Changes
- Removed all Kusto/Eventhouse/Eventstream functionality
- Package is now focused exclusively on Fabric Lakehouse SQL tools
- Removed Kusto-specific dependencies and environment variables

### Features
- Clean Lakehouse-only MCP server
- Simplified configuration with only 2 required environment variables
- Added UV_LINK_MODE to manifest for OneDrive compatibility

## 0.3.6 (2025-01-14)
### Features
- Added UV_LINK_MODE to MCP manifest
- Updated command to use uvx for proper installation
- Fixed OneDrive hardlink issues

## 0.3.5 (2025-01-14)
### Features  
- Cleaned documentation of old Kusto variable references
- Updated Quick Start Guide
- Fixed VS Code MCP configuration wizard issues

## 0.3.4 (2025-01-14)
### Features
- Changed server command name from fabric-lakehouse-mcp to fabric-lakehouse
- Simplified naming for better user experience

## 0.3.3 (2025-01-14)
### Features
- Added Python 3.13 support
- Updated pyodbc dependency to >=5.0.0 for Python 3.13 compatibility

## 0.3.2 (2025-01-14)
### Features
- Implemented Azure CLI authentication with DefaultAzureCredential
- Automatic token caching to avoid repeated authentication prompts

## 0.3.1 (2025-01-14)
### Breaking Changes
- Removed Kusto/RTI functionality for initial Lakehouse-only release
- Package renamed to fabric-lakehouse-mcp

### Features
- SQL Lakehouse tools for table listing and schema inspection
- Query History tools for viewing execution history

## 0.0.10 (Archived - Kusto Version)
### Other Changes
- Use docstring as tool description
- Add annotations (readonly, destructive)
- Add Attach to proc id + tracing pid on start so we can debug locally

## 0.0.9 (Archived - Kusto Version)
### Other Changes
- Removed bloat around deployment. Publishing regular package to PyPI
- Fixed PyPI pipeline

## 0.0.8 (Archived - Kusto Version)
### Other Changes
- Cleanup pyproject.toml
- Add logger that uses the stderr so that it could be seen in the MCP server logs
- Strip whitespaces from agent parameters 

## 0.0.7 (Archived - Kusto Version)
### Features
- Executable installed via pip
- Main functionality of the Kusto MCP server is implemented
- Readme includes instructions for manual installation of the server

