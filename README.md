# AI Chatbot

FastAPI backend for a chat application that stores conversations in PostgreSQL and delegates generation to an Ollama model.

## What It Does

- Creates and stores chat conversations and messages
- Persists available model names in the database
- Sends conversation history to Ollama for assistant responses
- Exposes a small REST API for chat and model management

## Tech Stack

- Python 3.14+
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Ollama

## Requirements

- Python 3.14 or newer
- PostgreSQL database
- Running Ollama instance

## Configuration

Create a `.env` file in the project root with:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/aichatbot
OLLAMA_API=http://localhost:11434
DEBUG=true
```

Environment variables:

- `DATABASE_URL`: SQLAlchemy connection string for PostgreSQL
- `OLLAMA_API`: Base URL for the Ollama server
- `DEBUG`: Enables FastAPI debug mode when set to `true`

## Installation

```bash
uv sync
```

If you are not using `uv`, install the dependencies from `pyproject.toml` with your preferred Python toolchain.

## Database Setup

Run the initial Alembic migration:

```bash
alembic upgrade head
```

The schema includes:

- `conversations`
- `messages`
- `models`

## Run The App

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

Base path: `/api/chats`

- `GET /conversation` - list conversations
- `GET /messages/{conversation_id}` - list messages for a conversation
- `GET /model` - list configured models
- `POST /create_conversation` - create a new conversation
- `POST /create_model` - create a new model record
- `POST /chat` - store a user message, send the conversation to Ollama, and store the assistant reply

## Request Shapes

### Create Model

```json
{
  "name": "qwen"
}
```

### Chat

```json
{
  "conversation_id": "00000000-0000-0000-0000-000000000000",
  "role": "user",
  "content": "Hello",
  "model": "OLLAMA"
}
```

For `/chat`, the `model` field is currently used as a provider selector. The provider implementation supports `OLLAMA`.

## Notes

- Conversations are identified with UUIDs.
- Messages are stored with timestamps and linked to a conversation by foreign key.
- The Ollama provider expects the conversation history in plain text prompt form.

## Project Layout

- `main.py` - FastAPI application entrypoint
- `src/routers` - API routes
- `src/services` - chat and provider logic
- `src/models` - SQLAlchemy models
- `src/schemas` - Pydantic request and response models
- `src/database` - database engine and session setup
- `alembic` - database migrations
