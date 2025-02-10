from crewai import Agent
from open_ai_client import llm
from tools import (
    MarketDataTool, OfficialTweetsTool, GetNewsTool, getTrendingTokensTool,
    GetCategoryMarketDataTool, GetSentimentAnalysisTool,
    GetTopGainersTool, GetTopLosersTool, InputTool
)

# Initialize tools
market_data_tool = MarketDataTool()
official_tweets_tool = OfficialTweetsTool()
news_tool = GetNewsTool()
trending_tokens_tool = getTrendingTokensTool()
category_market_data_tool = GetCategoryMarketDataTool()
sentiment_analysis_tool = GetSentimentAnalysisTool()
top_gainers_tool = GetTopGainersTool()
top_losers_tool = GetTopLosersTool()
tools = [market_data_tool, official_tweets_tool, news_tool, trending_tokens_tool, category_market_data_tool, sentiment_analysis_tool, top_gainers_tool, top_losers_tool]
# Now you can access each tool by name, e.g. tools["news"]


# Define the Decision-Making Agent (DMA) with function calling enabled
decision_agent = Agent(
    role="Decision-Making Agent",
    goal="You have access to multiple tools. only use the tools that are related to the user request.",
    backstory="You are SPECTgent, a superpowerful AI who is sarcastic about crypto.",
    tools=tools,  # Assign tools to the agent
    allow_delegation=True,
    llm=llm,  # Function calling requires GPT-4-turbo or GPT-3.5-turbo-1106+
    memory=True
)

# Define the User Interaction Agent (UIA)
user_interaction_agent = Agent(
    role="User Interaction Agent",
    goal="Process the user requests, and forward structured data. from {user_input}.",
    backstory="A friendly AI that ensures requests are well-structured",
    allow_delegation=False,
    tools=[InputTool()],  # Assign tools to the agent,
    llm=llm,
    memory=True
)

response_generator_agent = Agent(
    role="Response Generator Agent",
    goal="Generate a human-readable response from the decision agent's response taking into consideration the user input {user_input}.",
    backstory="A friendly AI that ensures the response is human-readable.",
    allow_delegation=False,
    llm=llm
)