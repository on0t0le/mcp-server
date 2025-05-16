from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from mcp.server.fastmcp import FastMCP
import os

# instantiate an MCP server client
mcp = FastMCP("Diagram Tools")

@mcp.tool()
def create_diagram(base_path: str, diagram_name: str, worker_name: str) -> bool:
    """Write content to a file.

    Args:
        diagram_name: Path to the file to write to (relative to project directory)
        content: Content to write to the file

    Returns:
        True if the file was written successfully
    """
    if not diagram_name or not isinstance(diagram_name, str):        
        return False

    if worker_name is None:        
        worker_name = ""

    if not isinstance(worker_name, str):       
        return False

    try:
        output_path = os.path.join(base_path, diagram_name)
        with Diagram("Grouped Workers", show=False, direction="TB", filename=output_path):
            # The diagram creation doesn't return a value, so we'll create it and return True if successful
            ELB("lb") >> EC2(worker_name) >> RDS("events")    
        return True

    except Exception as e:
        print(f"Error creating diagram: {e}")
        return False

if __name__ == "__main__":
    mcp.run(transport="stdio")
