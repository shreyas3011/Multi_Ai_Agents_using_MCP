# Multi AI Agents using MCP

A demonstration project showing how to use the Model Context Protocol (MCP) to create multi-server AI agents with LangChain and Groq.

## Overview

This project demonstrates how to build an AI agent that can interact with multiple MCP servers simultaneously:
- **Math Server**: Provides arithmetic operations (add, multiply) via stdio transport
- **Weather Server**: Provides weather information via HTTP transport

The client uses LangGraph to create a ReAct agent powered by Groq's LLM that can intelligently call tools from both servers.

## Project Structure

```
MCP_practice/
├── client.py              # Main client connecting to multiple MCP servers
├── server/
│   ├── mathserver.py      # MCP server with math operations (stdio)
│   └── weather.py         # MCP server with weather data (HTTP)
├── requirements.txt       # Python dependencies
├── myenv/                 # Virtual environment
└── README.md
```

## Features

- **Multi-Server Architecture**: Connects to multiple MCP servers with different transport protocols
- **Stdio Transport**: Math server uses standard input/output for communication
- **HTTP Transport**: Weather server uses streamable HTTP for communication
- **AI Agent Integration**: Uses LangGraph's ReAct agent with Groq LLM
- **Tool Orchestration**: Agent automatically selects and calls appropriate tools

## Prerequisites

- Python 3.12+
- Groq API Key

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd MCP_practice
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Linux/Mac
   # or
   myenv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

### 1. Start the Weather Server

In one terminal, start the weather server:
```bash
python3 server/weather.py
```

This will start an HTTP server on `http://localhost:8000/mcp`

### 2. Run the Client

In another terminal, run the client:
```bash
python3 client.py
```

The client will:
- Connect to both MCP servers (math and weather)
- Load available tools from each server
- Create an AI agent with access to all tools
- Execute a sample query: "what is (3+5)*6?"
- Display the agent's response

## MCP Servers

### Math Server (`server/mathserver.py`)
- **Transport**: stdio
- **Tools**:
  - `add(a, b)`: Adds two numbers
  - `multiply(a, b)`: Multiplies two numbers

### Weather Server (`server/weather.py`)
- **Transport**: streamable-http (port 8000)
- **Tools**:
  - `get_weather(location)`: Returns weather information for a location

## How It Works

1. **Client Setup**: The `MultiServerMCPClient` configures connections to multiple MCP servers with different transport protocols
2. **Tool Discovery**: Client fetches available tools from all connected servers
3. **Agent Creation**: A ReAct agent is created using Groq's LLM with access to all discovered tools
4. **Query Execution**: When given a task, the agent:
   - Analyzes the request
   - Selects appropriate tools
   - Executes tool calls
   - Returns the final result

## Technologies Used

- **MCP (Model Context Protocol)**: Standard protocol for AI-tool communication
- **FastMCP**: Framework for building MCP servers
- **LangChain**: Framework for building LLM applications
- **LangGraph**: Library for building stateful, multi-actor LLM applications
- **Groq**: Fast LLM inference platform
- **Python asyncio**: For asynchronous operations

## Troubleshooting

### Common Issues

1. **Weather server not running**
   - Ensure you start `server/weather.py` before running the client
   
2. **Module not found errors**
   - Make sure you've activated the virtual environment
   - Install all dependencies: `pip install -r requirements.txt`

3. **Groq API errors**
   - Verify your GROQ_API_KEY is set correctly in `.env`
   - Check that the model name is valid and not deprecated

4. **Port already in use**
   - The weather server uses port 8000 by default
   - If port 8000 is busy, modify the port in both `weather.py` and `client.py`

## License

MIT

## Contributing

Feel free to open issues or submit pull requests for improvements!