import requests
from crewai.tools import BaseTool
from logger import setup_logger
from typing import ClassVar


logger = setup_logger()


class InputTool(BaseTool):
    name: ClassVar[str] = "get_input"
    description: str = "Get input from the user."

    def _run(self, user_input: str):
        logger.info(f"Prompting user with: {user_input}")
        # user_input = input(prompt)
        return user_input


class OfficialTweetsTool(BaseTool):
    name: ClassVar[str] = "get_official_tweets"
    description: str = (
        "Ftech the latets tweets from the official account of a given username."
    )

    def _run(self, username: str):
        logger.info(f"Fetching official tweets for {username}")
        url = f"http://backend-277369611639.us-central1.run.app/get_official_tweets?username={username}"
        response = requests.get(url)
        return f"Here are the latest tweets from {username}: {response.json()}"


class MarketDataTool(BaseTool):
    name: ClassVar[str] = "get_market_data"
    description: str = "Fetch the current market data for a given token."

    def _run(self, token: str):
        logger.info("Fetching market data for {token}")
        url = (
            f"https://search-serv-277369611639.us-central1.run.app/fetch?query={token}"
        )
        response = requests.get(url)
        return f"Here is the market data for {token}: {response.json() }"


class GetNewsTool(BaseTool):
    name: ClassVar[str] = "get_news"
    description: str = "Fetch the latest news about cryptocurrencies."

    def _run(self):
        logger.info("Fetching the latest news.")
        url = (
            "https://us-central1-third-opus-411016.cloudfunctions.net/"
            "SearchEngineApiV4/news?search=crypto&page_size=30"
        )
        response = requests.get(url)
        return f"Here are the latest news articles: {response.json()}"


class getTrendingTokensTool(BaseTool):
    name: ClassVar[str] = "get_trending_tokens"
    description: str = "Fetch the trending tokens in the market."

    def _run(self):
        logger.info("Fetching the trending tokens.")
        url = (
            "https://us-central1-third-opus-411016.cloudfunctions.net/SearchEngineApiV4/"
            "x_trending"
        )
        response = requests.get(url)
        return f"Here are the trending tokens: {response.json()}"


class GetSentimentAnalysisTool(BaseTool):
    name: ClassVar[str] = "get_sentiment_analysis"
    description: str = "Analyze the sentiment of the market for a given token."

    def _run(self, token: str):
        logger.info(f"Analyzing the sentiment for {token}")
        url = (
            f"https://us-central1-third-opus-411016.cloudfunctions.net/"
            f"SearchEngineApiV4/get_final_sent?query={token}"
        )
        response = requests.get(url)
        return f"Here is the sentiment analysis for {token}: {response.json()}"


class GetTopGainersTool(BaseTool):
    name: ClassVar[str] = "get_top_gainers"
    description: str = "Fetch the top gainers in the market."

    def _run(self):
        logger.info("Fetching the top gainers.")
        url = "https://us-central1-third-opus-411016.cloudfunctions.net/SearchEngineApiV4/get_top_gainers"
        response = requests.get(url)
        return f"Here are the top gainers: {response.json()}"


class GetTopLosersTool(BaseTool):
    name: ClassVar[str] = "get_top_losers"
    description: str = "Fetch the top losers in the market."

    def _run(self):
        logger.info("Fetching the top losers.")
        url = "https://us-central1-third-opus-411016.cloudfunctions.net/SearchEngineApiV4/get_top_losers"
        response = requests.get(url)
        return f"Here are the top losers: {response.json()}"


class GetCategoryMarketDataTool(BaseTool):
    name: ClassVar[str] = "get_category_market_data"
    description: str = "Fetch the market data for a given category."

    def _run(self, category: str):
        logger.info(f"Fetching market data for {category}")
        url = f"https://us-central1-third-opus-411016.cloudfunctions.net/SearchEngineApiV4/category_market_data?query={category}"
        response = requests.get(url)
        return f"Here is the market data for {category}: {response.json()}"
