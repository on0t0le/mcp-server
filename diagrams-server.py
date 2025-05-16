from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from mcp.server.fastmcp import FastMCP

# instantiate an MCP server client
mcp = FastMCP("Diagram Tools")

@mcp.tool()
def create_diagram(diagram_name: str, worker_name: str) -> bool:
    """Write content to a file.

    Args:
        diagram_name: Path to the file to write to (relative to project directory)
        content: Content to write to the file

    Returns:
        True if the file was written successfully
    """
    if not diagram_name or not isinstance(diagram_name, str):        
        raise ValueError(f"File path must be a non-empty string, got {type(diagram_name)}")

    if worker_name is None:        
        worker_name = ""

    if not isinstance(worker_name, str):       
        raise ValueError(f"Worker must be a string, got {type(worker_name)}")

    try:
        with Diagram("Grouped Workers", show=False, direction="TB", filename=diagram_name):
            success = ELB("lb") >> EC2(worker_name) >> RDS("events")    
        return success

    except Exception as e:
        print(f"Error creating diagram: {e}")
        return False

if __name__ == "__main__":
    mcp.run(transport="stdio")