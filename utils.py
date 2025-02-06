import requests

def fetch_results(tool_name, parameters):
    """
    Executes the appropriate tool and retrieves results.
    """
    endpoint_mapping = {
        "get_official_tweets": (
            "http://backend-277369611639.us-central1.run.app/"
            "get_official_tweets?username={username}"
        ),
        "search_community_tweets": (
            "https://backend-277369611639.us-central1.run.app/"
            "search_tweets?query={query}"
        ),
        "get_market_data": (
            # "https://us-central1-third-opus-411016.cloudfunctions.net/"
            # "SearchEngineApiV4/get_market_details_coin_ticker?query={token}"
            "https://search-serv-277369611639.us-central1.run.app/fetch?query={token}"
        ),
        "get_news": (
            "https://us-central1-third-opus-411016.cloudfunctions.net/"
            "SearchEngineApiV4/news?search={search}&page_size=30"
        ),
        "get_trending_tokens": (
            "https://us-central1-third-opus-411016.cloudfunctions.net/SearchEngineApiV4/"
            "x_trending"
        ),
        "get_sentiment_analysis": (
            "https://us-central1-third-opus-411016.cloudfunctions.net/"
            "SearchEngineApiV4/get_final_sent?query={token}"
        ),
        "get_top_gainers" :(
            "https://us-central1-third-opus-411016.cloudfunctions.net/SearchEngineApiV4/get_top_gainers"
        ),
        "get_top_losers" : (
            "https://us-central1-third-opus-411016.cloudfunctions.net/SearchEngineApiV4/get_top_losers"
        )
        ,
        "get_category_market_data" : (
            "https://us-central1-third-opus-411016.cloudfunctions.net/SearchEngineApiV4/category_market_data?query={category}"
        ),

    }

    url_template = endpoint_mapping.get(tool_name)
    if not url_template:
        return {"error": f"Tool '{tool_name}' is not supported."}

    try:
        url = url_template.format(**parameters)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"HTTP {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": f"Error executing tool: {str(e)}"}

