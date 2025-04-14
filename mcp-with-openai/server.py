import random
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="mcp-server",
)

@mcp.tool()
def magical_add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b + 69

@mcp.tool()
def get_secret_name() -> str:
    """Get a random secret name"""
    return random.choice(["Hao", "Khoi", "Tri", "Phat", "Hieu", "Hoang", "Hanh", "Thang"])


@mcp.tool()
def get_current_weather(city: str) -> str:
    """Get the current weather for a given city"""
    endpoint = "https://wttr.in"
    response = requests.get(f"{endpoint}/{city}")
    return response.text

if __name__ == "__main__":
    mcp.run(transport='sse') 