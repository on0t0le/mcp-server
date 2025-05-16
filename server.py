from mcp.server.fastmcp import FastMCP

# instantiate an MCP server client
mcp = FastMCP("MCP Tools")


# Register a tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers and return the result"""
    return a + b


if __name__ == "__main__":
    mcp.run(transport="stdio")