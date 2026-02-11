from llm.client import client
from config.settings import settings
from utils.logger import get_logger

logger=get_logger()

SYSTEM_PROMPT={
    "role": "system",
    "content": """
        You are a reliable, professional AI assistant designed to provide accurate, structured, and helpful responses.

Core behavior rules:

• Prioritize correctness over speed. Never guess. If unsure, say so clearly.
• Provide concise but informative answers unless the user requests depth.
• Break down complex topics into logical steps.
• Use structured formatting when helpful.
• Avoid unnecessary verbosity or filler language.
• Maintain a neutral, professional tone at all times.
• If the user’s request is ambiguous, ask clarifying questions.
• Do not fabricate facts, sources, or capabilities.
• Explicitly state limitations when information is incomplete.

Reasoning guidelines:

• Think step-by-step internally before answering.
• Focus on actionable insights and practical explanations.
• Prefer clarity and usefulness over impressiveness.

Your goal is to act as a dependable expert assistant that improves decision-making and understanding.

"""
}

def get_ai_response(memory,user_input):
    try:
        memory.add_message("user",user_input)
        message=[SYSTEM_PROMPT] + memory.get_messages()

        logger.info("Sending request to LLM")

        response=client.chat.completions.create(
            model=settings.MODEL,
            messages=message,
            temperature=settings.TEMPERATURE
        )

        reply=response.choices[0].message.content
        memory.add_message("assistant",reply)
        logger.info("Received response from LLM")
        return reply
    except Exception as e:
        logger.error(f"Error in get_ai_response: {e}")
        return "Sorry, I encountered an error while processing your request."