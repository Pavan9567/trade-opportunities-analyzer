from google import genai
from app.core.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

async def analyze_data(sector, data):

    prompt = f"""
    You are a financial market analyst specializing in Indian sectors.

    Analyze the {sector} sector using the data below:

    {data}

    Provide:
    1. Market Overview
    2. Key Trends (bullet points)
    3. Trade Opportunities (actionable)
    4. Risks
    5. Outlook
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text