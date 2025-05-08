import yfinance as yf
from fastmcp import FastMCP
from pandas import DataFrame

# Give the FastMCP server a name
mcp = FastMCP("stocks")

# This example just uses tools, but FastMCP also offers additional capabilities
@mcp.tool()
def fetch_stock_info(symbol: str) -> dict:                  # Output is a dictionary
    """Get stock general company information."""
    stock = yf.Ticker(symbol)
    return stock.info

@mcp.tool()
def fetch_quarterly_financials(symbol: str) -> DataFrame :  # Output is a Panda DataFrame
    """Get stock quarterly financials."""
    stock = yf.Ticker(symbol)
    return stock.quarterly_financials.T                     # "T" stands for transpose

@mcp.tool()
def fetch_annual_financials(symbol: str) -> DataFrame:      # Output is a Panda DataFrame
    """Get stock annual financials."""
    stock = yf.Ticker(symbol)
    return stock.financials.T                               # "T" stands for transpose

# The transport uses Python standard input/output (stdio) for a local MCP server
if __name__ == "__main__":
    mcp.run(transport="stdio")
