from src.services.provider.ollama_provider import send_ollama
from src.models.conversation import Conversation


def _conversation_to_prompt(message: Conversation) -> str:
    return "\n".join(f"{entry.role}: {entry.content}" for entry in message.messages)


def send_message(message: Conversation, provider: str):

    if provider == 'OLLAMA':
        response = send_ollama(_conversation_to_prompt(message))
        return response
    raise ValueError(f"Unsupported provider: {provider}")
    
