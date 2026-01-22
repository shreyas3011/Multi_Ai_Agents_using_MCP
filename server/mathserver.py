from mcp.server.fastmcp import FastMCP

mcp=FastMCP("mathserver")

@mcp.tool()
def add(a:int,b:int) -> int:
    """_summary_
    add twonumbers
    
    """
    return a+b 

@mcp.tool()
def multply(a:int,b:int) -> int:
    """summary
    multiply two numbers
    
    """
    return a*b



if __name__=="__main__":
    mcp.run(transport="stdio")