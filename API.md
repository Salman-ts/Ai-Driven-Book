# AI Book API Documentation

## Authentication
- **POST** `/auth/signup`
- **POST** `/auth/signin`
- **POST** `/auth/refresh`
- **GET** `/auth/me`

## RAG & Chat
- **POST** `/chat/message`
  - Body: `{ "query": "string", "history": [...] }`
  - Returns: Stream of text + citations.

## Personalization
- **POST** `/content/personalize`
  - Body: `{ "content": "string", "chapter_id": 1 }`
  - Uses User Profile implicit in session.
