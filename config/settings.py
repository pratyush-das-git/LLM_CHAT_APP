import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL= "gpt-4.1-mini"
    MAX_HISTORY = 10
    TEMPERATURE = 0.7

settings = Settings()
