FUNC_TOOLS = [

    # Do we have to provide the Exact username there are no alternatives ? 

    {
        "type": "function",
        "function": {
            "name": "get_official_tweets",
            "description": "Fetch the latest official tweets of a project or influencer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string",
                        "description": "The username to fetch tweets for (e.g., ElonMusk, RealDonaldTrump)."
                    }
                },
                "required": ["username"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "search_community_tweets",
            "description": "Find community and users tweets about a token (e.g., $TOKEN).",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The token or topic to search for (e.g., $BTC)."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_market_data",
            "description": "Fetch market data (price, chart, volume, market cap, etc.) for a mentioned token if its spect or $spect then token = SPECTRE.",
            "parameters": {
                "type": "object",
                "properties": {
                    "token": {
                        "type": "string",
                        "description": "The token to fetch data for (e.g., ETH, BTC, etc.)."
                    }
                },
                "required": ["token"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_news",
            "description": "Returns the current market news. Does not contain market data such as price, etc , prioritze it without a parameter unless if the user asks for it ",
            "parameters": {
                "type": "object",
                "properties": {
                    "search": {
                        "type": "string",
                        "description": (
                            "The search term or token or blank for a broader search prioritize blank (e.g., 'crypto'). "
                            "Use '%20' for spaces (e.g. 'Elon%20Musk')."
                        )
                    }
                },
                "required": ["search"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_trending_tokens",
            "description": "Fetch trending tokens on Twitter (X).",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    
    {
        "type": "function",
        "function": {
            "name": "get_sentiment_analysis",
            "description": "Fetch the sentiment score for a token if its spect or $spect then token use SPECTRE",
            "parameters": {
                "type": "object",
                "properties": {
                    "token": {
                        "type": "string",
                        "description": "The token to analyze sentiment for (e.g., DOGE)."
                    }
                },
                "required": ["token"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_top_gainers",
            "description": "returns the current top gainers in the market  prioritze it without a parameter unless if the user asks for it",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_top_losers",
            "description": "Returns the current top losers in the market  prioritze it without a parameter unless if the user asks for it",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_category_market_data",
            "description": "Fetch market data about a given for a mentioned category",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "The category to fetch data for (e.g., AI Agents, Asset Manager, etc.)."
                    }
                },
                "required": ["category"]
            }
        }
    }
]