from duckduckgo_search import DDGS

async def fetch_news(sector: str):
    query = f"{sector} sector India latest news"

    results = []

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                title = str(r.get("title", ""))
                body = str(r.get("body", ""))

                results.append(f"Title: {title}\nSummary: {body}\n")

    except Exception as e:
        print("DuckDuckGo error:", str(e))
        return "No data available"

    return "\n".join(results) if results else "No data available"