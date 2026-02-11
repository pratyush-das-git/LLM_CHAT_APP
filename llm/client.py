from openai import OpenAI
from config.settings import settings

client=OpenAI(
    api_key=settings.API_KEY
    )