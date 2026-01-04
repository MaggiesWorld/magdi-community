Magdi-ai Api Reference
?? Magdi-AI API Reference

This document describes the Magdi-AI backend API, including request formats, responses, and expected HTTP return codes.

?? Base URL

Local development:

http://localhost:5000
?? Authentication

Authentication is handled via JWT after login.

POST /login

Authenticate a user.

Request

{
  "email": "user@example.com",
  "password": "password"
}

Responses

200 OK – Authenticated

401 Unauthorized – Invalid credentials

POST /register

Register a new user.

Request

{
  "email": "user@example.com",
  "password": "password",
  "confirmPassword": "password"
}

Responses

201 Created

400 Bad Request

GET /validate-user

Validates an authenticated user session.

Headers

Authorization: Bearer <JWT>

Responses

200 OK

401 Unauthorized

?? Conversation Lifecycle
POST /select

Select an agent category.

Request

{
  "user_id": 1,
  "category": "test_generation"
}

Responses

200 OK

400 Bad Request

POST /start_conversation

Start a new persistent conversation.

Request

{
  "user_id": 1,
  "assistant_id": "asst_xxx",
  "category": "test_generation",
  "agent_name": "MagdiPartner",
  "llm_model": "gpt-4"
}

Responses

200 OK (returns conversation_id)

400 Bad Request

POST /conversation/upload

Upload files into an active conversation context.

Content-Type

multipart/form-data

Form Fields

user_id (int, required)

conversation_id (uuid, required)

files[] (file, optional)

Responses

200 OK

400 Bad Request

404 Conversation not found

POST /chat

Send a message to the active agent.

?? Important: This endpoint requires multipart/form-data, even when no files are uploaded.

Content-Type

multipart/form-data

Form Fields

user_id (int, required)

category (string, required)

message (string, required)

conversation_id (uuid, required)

llm_model (string, optional)

files[] (file, optional)

Responses

200 OK

400 Bad Request

404 Conversation not found

429 Rate limit exceeded

500 Server error

POST /end_conversation

End a conversation.

Request

{
  "conversation_id": "uuid"
}

Responses

200 OK

400 Bad Request

?? Project Artifacts
GET /api/download

Download a generated or updated project ZIP.

Query Parameters

zip_id (string, required)

disposable=1 (optional)

Responses

200 OK – ZIP file download

404 Not found

?? Usage & System APIs
GET /usage

Query Parameters:

user_id (int)

Responses

200 OK

GET /config/rate-limit

Returns daily token allowance.

Responses

200 OK

GET /version

Returns backend version information.

Responses

200 OK

GET /metrics

Prometheus-compatible metrics endpoint.

Responses

200 OK

GET /metrics-update-visitors

Updates visitor metrics.

Responses

200 OK

GET /metrics-update-tokens

Updates token usage metrics.

Responses

200 OK

? Common Error Codes
Code	Meaning
400	Invalid request or format
401	Unauthorized
404	Resource not found
429	Rate limit exceeded
500	Internal server error
?? Notes

Conversations are stateful and scoped per user

Project artifacts are scoped per conversation

Generated ZIPs may be disposable

/chat must use multipart encoding

Yes — excellent call ??
Canvas is exactly the right tool for this.

? I’ve now placed the entire API Reference into Canvas as a single, properly formatted document.
Everything is clean Markdown, consistent code blocks, and easy to:

Select all

Copy once

Paste directly into docs/API_REFERENCE.md

No broken blocks, no inline leakage.

What we have now

?? Canvas document: Magdi-AI API Reference

Fully structured

All requests / responses in proper code fences

Ready for version control

Suggested next micro-steps (optional)

Add a short header to README:

See docs/API_REFERENCE.md for full backend API documentation.


Later (not now):

OpenAPI spec

Postman collection

SDK hints