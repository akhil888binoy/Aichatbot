from src.services.provider.ollama_provider import send_ollama
from src.models.conversation import Conversation
from src.schemas.chat import ChatResponse

def _conversation_to_prompt(message: list[ChatResponse]) -> str:
    return "\n".join(f"{entry.role}: {entry.content}" for entry in message)

def send_message(message: list[ChatResponse], provider: str) -> str:
    if provider == 'OLLAMA':
        response = send_ollama(_conversation_to_prompt(message))
        return response
    raise ValueError(f"Unsupported provider: {provider}")