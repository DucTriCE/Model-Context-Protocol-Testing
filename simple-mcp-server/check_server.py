from mcp import ClientSession
from mcp.client.sse import sse_client

async def check():
    async with sse_client("http://192.168.72.174:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            # List avail tool
            tools = await session.list_tools()
            print(tools)

            # Call tool
            a = 4
            b = 6
            result = await session.call_tool("add", arguments={"a": a, "b": b})
            print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(check())