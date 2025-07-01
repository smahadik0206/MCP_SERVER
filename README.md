# 🌦️ Git_Weather MCP Server

The **Git_Weather** MCP Server is an AI-powered module that integrates with the [MCP Server Framework](https://github.com/smahadik0206/MCP_SERVER.git). It is built to process weather-related tasks via natural language using the `uvx` runner.

---

## 📦 Requirements

Before you begin, ensure the following:

- **Python 3.8+**
- **Git installed**
- **uvx installed**

Install `uvx` using pip:

```bash
pip install uvicornx


To configure and install the Git_Weather server, use this JSON snippet in your MCP setup:

{
  "mcpServers": {
    "Git_Weather": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/smahadik0206/MCP_SERVER.git",
        "mcp-server"
      ]
    }
  }
}

Or run it directly using

```bash
uvx --from git+https://github.com/smahadik0206/MCP_SERVER.git mcp-server
