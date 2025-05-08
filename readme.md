# MCP (Model Context Protocol) server and client using FastMCP and LangChain

This example builds a local [MCP](https://modelcontextprotocol.io/introduction) server using [FastMCP](https://github.com/jlowin/fastmcp) and creates a LangChain Artificial Intelligence agent that uses the tools defined in the MCP server.

Creating MCP servers usually requires a lot of boilerplate code and configuration. FastMCP makes it much easier to set up MCP servers.

LangChain MCP adapters can easily connect to local or external MCP servers.

This example uses FastMCP to create a local MCP server and then uses LangChain MCP adapters on the client side. Because this example uses an OpenAI Large Language Model (LLM), it also uses LangChain's OpenAI implementation to communicate with the LLM. It creates a LangGraph ReAct (Reasoning and Acting) agent. Asyncio is needed for asynchronous functions.

Because this example uses a local MCP server, the connection ("transport") uses stdio (Python standard input/output streams). An external MCP server would require Server-Sent Events (SSE), or WebSockets transport instead of stdio.

The LLM can be asked anything about a stock. The LLM will then go ahead and call the tools defined in the MCP server, collect all the information, and answer with the collected information.

This example asks:

```
What company uses the stock ticker META and how did this company's revenue develop over the last quarters and years?
```

[YFinance](https://github.com/ranaroussi/yfinance) provides stock market tools for the MCP server. YFinance is a Python library used for accessing financial data from Yahoo Finance. YFinance doesn't require an API key.

## Required API key for this example

You need an OpenAI API key for this example. [Get your OpenAI API key here](https://platform.openai.com/login). Insert the OpenAI API key into the `.env.example` file and then rename this file to just `.env` (remove the ".example" ending).

## Run this example

Run the application from command line with:

```
python mcp_client.py
```

## Example results

As you can tell from the answer, all 3 tools defined in the MCP server have been used:

```
Match 1:
{"address1": "1 Meta Way", "city": "Menlo Park", "state": "CA", "zip": "94025", "country": "United States", "phone": "650 543 4800", "website": "https://investor.atmeta.com", "industry": "Internet Content & Information", "industryKey": "internet-content-information", "industryDisp": "Internet Content & Information", "sector": "Communication Services", "sectorKey": "communication-services", "sectorDisp": "Communication Services", "longBusinessSummary": "Meta Platforms, Inc. engages in the development of products that enable people to connect and share with friends and family through mobile devices, personal computers, virtual reality and mixed reality headsets, augmented reality, and wearables worldwide. It operates through two segments, Family of Apps (FoA) and Reality Labs (RL). The FoA segment offers Facebook, which enables people to build community through feed, reels, stories, groups, marketplace, and other; Instagram that brings people closer through instagram feed, stories, reels, live, and messaging; Messenger, a messaging application for people to connect with friends, family, communities, and businesses across platforms and devices through text, audio, and video calls; Threads, an application for text-based updates and public conversations; and WhatsApp, a messaging application that is used by people and businesses to communicate and transact in a private way. The RL segment provides virtual, augmented, and mixed reality related products comprising consumer hardware, software, and content that help people feel connected, anytime, and anywhere. The company was formerly known as Facebook, Inc. and changed its name to Meta Platforms, Inc. in October 2021. The company was incorporated in 2004 and is headquartered in Menlo Park, California.", "fullTimeEmployees": 76834, "companyOfficers": [{"maxAge": 1, "name": "Mr. Mark Elliot Zuckerberg", "age": 40, "title": "Founder, Chairman & CEO", "yearBorn": 1984, "fiscalYear": 2024, "totalPay": 27219874, "exercisedValue": 0, "unexercisedValue": 0}, {"maxAge": 1, "name": "Ms. Susan J. S. Li", "age": 38, "title": "Chief Financial Officer", "yearBorn": 1986, "fiscalYear": 2024, "totalPay": 1948846, "exercisedValue": 0, "unexercisedValue": 0}, {"maxAge": 1, "name": "Mr. Javier  Olivan", "age": 47, "title": "Chief Operating Officer", "yearBorn": 1977, "fiscalYear": 2024, "totalPay": 3835042, "exercisedValue": 0, "unexercisedValue": 0}, {"maxAge": 1, "name": "Mr. Andrew  Bosworth", "age": 42, "title": "Chief Technology Officer", "yearBorn": 1982, "fiscalYear": 2024, "totalPay": 1923184, "exercisedValue": 0, "unexercisedValue": 0}, {"maxAge": 1, "name": "Mr. Christopher K. Cox", "age": 41, "title": "Chief Product Officer", "yearBorn": 1983, "fiscalYear": 2024, "totalPay": 1937677, "exercisedValue": 0, "unexercisedValue": 0}, {"maxAge": 1, "name": "Mr. Dana  White", "title": "Independent Director", "fiscalYear": 2024, "totalPay": 272, "exercisedValue": 0, "unexercisedValue": 0}, {"maxAge": 1, "name": "Mr. Aaron A. Anderson", "title": "Chief Accounting Officer", "fiscalYear": 2024, "exercisedValue": 0, "unexercisedValue": 0}, {"maxAge": 1, "name": "Mr. Atish  Banerjea", "age": 58, "title": "Chief Information Officer", "yearBorn": 1966, "fiscalYear": 2024, "exercisedValue": 0, "unexercisedValue": 0}, {"maxAge": 1, "name": "Ms. Jennifer G. Newstead J.D.", "age": 53, "title": "Chief Legal Officer", "yearBorn": 1971, "fiscalYear": 2024, "totalPay": 3079624, "exercisedValue": 0, "unexercisedValue": 0}, {"maxAge": 1, "name": "Mr. Henry T. A. Moniz", "age": 59, "title": "Chief Compliance Officer", "yearBorn": 1965, "fiscalYear": 2024, "exercisedValue": 0, "unexercisedValue": 0}], "auditRisk": 10, "boardRisk": 10, "compensationRisk": 10, "shareHolderRightsRisk": 10, "overallRisk": 10, "governanceEpochDate": 1746057600, "compensationAsOfEpochDate": 1735603200, "executiveTeam": [], "maxAge": 86400, "priceHint": 2, "previousClose": 599.27, "open": 592.525, "dayLow": 586.58, "dayHigh": 596.0, "regularMarketPreviousClose": 599.27, "regularMarketOpen": 592.525, "regularMarketDayLow": 586.58, "regularMarketDayHigh": 596.0, "dividendRate": 2.1, "dividendYield": 0.36, "exDividendDate": 1741910400, "payoutRatio": 0.0792, "beta": 1.237, "trailingPE": 22.932838, "forwardPE": 23.213835, "volume": 10332250, "regularMarketVolume": 10332250, "averageVolume": 18515718, "averageVolume10days": 18570790, "averageDailyVolume10Day": 18570790, "bid": 586.18, "ask": 588.22, "bidSize": 1, "askSize": 1, "marketCap": 1506761506816, "fiftyTwoWeekLow": 442.65, "fiftyTwoWeekHigh": 740.91, "priceToSalesTrailing12Months": 8.844573, "fiftyDayAverage": 580.1932, "twoHundredDayAverage": 580.8713, "trailingAnnualDividendRate": 2.025, "trailingAnnualDividendYield": 0.0033791114, "currency": "USD", "tradeable": false, "enterpriseValue": 1455978577920, "profitMargins": 0.39113998, "floatShares": 2166796937, "sharesOutstanding": 2181270016, "sharesShort": 31512402, "sharesShortPriorMonth": 24545066, "sharesShortPreviousMonthDate": 1741910400, "dateShortInterest": 1744675200, "sharesPercentSharesOut": 0.0125, "heldPercentInsiders": 0.00089, "heldPercentInstitutions": 0.80194, "shortRatio": 1.45, "shortPercentOfFloat": 0.0145000005, "impliedSharesOutstanding": 2565530112, "bookValue": 73.337, "priceToBook": 8.008372, "lastFiscalYearEnd": 1735603200, "nextFiscalYearEnd": 1767139200, "mostRecentQuarter": 1743379200, "earningsQuarterlyGrowth": 0.346, "netIncomeToCommon": 66635001856, "trailingEps": 25.61, "forwardEps": 25.3, "enterpriseToRevenue": 8.546, "enterpriseToEbitda": 16.549, "52WeekChange": 0.24272108, "SandP52WeekChange": 0.08081472, "lastDividendValue": 0.525, "lastDividendDate": 1741910400, "quoteType": "EQUITY", "currentPrice": 587.31, "targetHighPrice": 935.0, "targetLowPrice": 466.0, "targetMeanPrice": 703.8915, "targetMedianPrice": 690.0, "recommendationMean": 1.45588, "recommendationKey": "strong_buy", "numberOfAnalystOpinions": 62, "totalCash": 70229999616, "totalCashPerShare": 27.932, "ebitda": 87979999232, "totalDebt": 49519001600, "quickRatio": 2.501, "currentRatio": 2.662, "totalRevenue": 170359996416, "debtToEquity": 26.763, "revenuePerShare": 67.349, "returnOnAssets": 0.17879999, "returnOnEquity": 0.39835, "grossProfits": 139297996800, "freeCashflow": 36658999296, "operatingCashflow": 96108003328, "earningsGrowth": 0.365, "revenueGrowth": 0.161, "grossMargins": 0.81767, "ebitdaMargins": 0.51644003, "operatingMargins": 0.41487, "financialCurrency": "USD", "symbol": "META", "language": "en-US", "region": "US", "typeDisp": "Equity", "quoteSourceName": "Nasdaq Real Time Price", "triggerable": true, "customPriceAlertConfidence": "HIGH", "longName": "Meta Platforms, Inc.", "exchange": "NMS", "messageBoardId": "finmb_20765463", "exchangeTimezoneName": "America/New_York", "exchangeTimezoneShortName": "EDT", "gmtOffSetMilliseconds": -14400000, "market": "us_market", "esgPopulated": false, "regularMarketChangePercent": -1.9957651, "regularMarketPrice": 587.31, "shortName": "Meta Platforms, Inc.", "hasPrePostMarketData": true, "firstTradeDateMilliseconds": 1337347800000, "postMarketChangePercent": 0.929666, "postMarketPrice": 592.77, "postMarketChange": 5.46002, "regularMarketChange": -11.960022, "regularMarketDayRange": "586.58 - 596.0", "fullExchangeName": "NasdaqGS", "averageDailyVolume3Month": 18515718, "fiftyTwoWeekLowChange": 144.66, "fiftyTwoWeekLowChangePercent": 0.3268045, "fiftyTwoWeekRange": "442.65 - 740.91", "fiftyTwoWeekHighChange": -153.59998, "fiftyTwoWeekHighChangePercent": -0.2073126, "fiftyTwoWeekChangePercent": 24.272108, "dividendDate": 1742947200, "earningsTimestamp": 1746043503, "earningsTimestampStart": 1753786740, "earningsTimestampEnd": 1754308800, "earningsCallTimestampStart": 1746046800, "earningsCallTimestampEnd": 1746046800, "isEarningsDateEstimate": true, "epsTrailingTwelveMonths": 25.61, "epsForward": 25.3, "epsCurrentYear": 25.53311, "priceEpsCurrentYear": 23.001898, "fiftyDayAverageChange": 7.1168213, "fiftyDayAverageChangePercent": 0.012266296, "twoHundredDayAverageChange": 6.4387207, "twoHundredDayAverageChangePercent": 0.011084591, "sourceInterval": 15, "exchangeDataDelayedBy": 0, "ipoExpectedDate": "2022-06-09", "averageAnalystRating": "1.5 - Strong Buy", "cryptoTradeable": false, "marketState": "PREPRE", "corporateActions": [], "postMarketTime": 1746575989, "regularMarketTime": 1746561600, "displayName": "Meta Platforms", "trailingPegRatio": 1.9916}

Match 2:
           Tax Effect Of Unusual Items  ... Operating Revenue
2025-03-31             21935371.559134  ...     41804000000.0
2024-12-31               -44365234.375  ...     47866000000.0
2024-09-30                   1320000.0  ...     40155000000.0
2024-06-30                 -18480000.0  ...     38682000000.0
2024-03-31            -18929140.520341  ...     36075000000.0

[5 rows x 45 columns]

Match 3:
           Tax Effect Of Unusual Items  ... Operating Revenue
2024-12-31                 -81420000.0  ...    162779000000.0
2023-12-31                 -64416000.0  ...    133844000000.0
2022-12-31                 -15795000.0  ...    115801000000.0
2021-12-31                 -23380000.0  ...    117208000000.0
2020-12-31                         NaN  ...               NaN

[5 rows x 48 columns]
```
