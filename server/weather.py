from mcp.server.fastmcp import FastMCP

mcp=FastMCP("weather_server")

@mcp.tool()
async def get_weather(location:str) ->str:
    """summary
    get weather update fro the location"""

    return f"The weather in {location} is sunny with a high of 25°C."

if __name__=="__main__":
    mcp.run(transport="streamable-http")