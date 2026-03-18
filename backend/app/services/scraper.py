from duckduckgo_search import DDGS

async def fetch_news(sector: str):
    query = f"{sector} sector India latest news market trends"

    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=7):
            results.append(
                f"Title: {r.get('title')}\nSummary: {r.get('body')}\n"
            )

    return "\n".join(results)