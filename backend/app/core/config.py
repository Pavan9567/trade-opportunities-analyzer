import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")
    RATE_LIMIT = os.getenv("RATE_LIMIT", "5/minute")

settings = Settings()