import asyncio
import os
import re
from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import warnings
warnings.filterwarnings('ignore')

# Environment variables
load_dotenv()
openai_api_key = os.environ["OPENAI_API_KEY"]

model = ChatOpenAI(model="gpt-4o")
# Parameters include how to run the server (using Python) and the program code file to execute
server_params = StdioServerParameters(
    command="python",
    args=["mcp_server.py"],
)

# The "main()" function is asynchronous, because calling the MCP tools is also asynchronous
async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            # Create a LangGraph ReAct (Reasoning and Acting) agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages":"What company uses the stock ticker META " \
                "and how did this company's revenue develop over the last quarters and years?"})
            # Define a regex pattern with:
            # - Literal match for ToolMessage(content='
            # - A non-greedy capture group for everything up to the next '
            pattern = r"ToolMessage\(content='(.*?)'"
            # Use re.findall with DOTALL so '.' matches newlines too
            matches = re.findall(pattern, str(agent_response), flags=re.DOTALL)
            # Display all extracted contents
            for i, content in enumerate(matches, 1):
                # Replace literal "\n" with actual newline characters
                content = content.replace("\\n", "\n")
                print(f"Match {i}:\n{content}\n")

if __name__ == "__main__":
    asyncio.run(main())
