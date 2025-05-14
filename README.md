# 🤖 MagDi AI – The AI Assistant for QA and Test Automation

MagDi AI is a smart, OpenAI-powered assistant designed to streamline workflows for professionals in **Software Quality Assurance (QA)** and **Test Automation (TA)**. With features like intelligent query routing, persistent chat threads, and containerized deployment, MagDi helps teams get answers, generate documentation, and boost productivity.

---

## 🚀 Features

- 🔍 **Intelligent Query Routing**: Classifies questions and routes them to the appropriate QA or TA assistant.
- 💬 **Persistent Sessions**: Maintains user-specific conversation history via threads.
- 🗃️ **PostgreSQL Integration**: Tracks assistant metadata, threads, and users.
- 🔒 **Environment Separation**: Clear dev vs. prod config with `.env` and `.env.prod`.
- 🐳 **Dockerized Deployment**: Spin up development or production environments in one command.
- ⚙️ **Pluggable Architecture**: Easily extend agents, tools, and interfaces.
- 🧪 **Test-Friendly**: Built-in unit tests and support for Postman.

---

## 🏗️ Tech Stack

- **Frontend**: React + Vite + Tailwind CSS
- **Backend**: Python (Flask), Gunicorn
- **AI**: OpenAI Assistants API
- **Database**: PostgreSQL
- **Containerization**: Docker + Docker Compose
- **Environment**: `dotenv`, `.env`, `.env.prod`

---

## ⚙️ Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- OpenAI API key
- Secret key for user auth (Flask)

---

## 🛠️ Setup and Run

### 1. Clone the Repository

```bash
git clone https://github.com/MaggiesWorld/magdi-ai.git
cd magdi-ai

### 2. Setup Environment Variables

A.  copy .env.example to .env.prod

B.  open .env.prod and update the following:

    i.  OPENAI_API_KEY=your_key_here
    ii. X_API_KEY=your_secret_key

Note: The X_API_KEY is used for user authentication in the backend.
You can generate the secret using the command,

python -c "import secrets; print(secrets.token_hex(32))"

### 3. Run MagDi Community in Production Mode

docker-compose --env-file .env.prod -f docker-compose.prod.yml up

This will launch:

ghcr.io/<your-org>/magdi-ai-frontend:alpha

ghcr.io/<your-org>/magdi-ai-backend:alpha

App will be available at: http://localhost:3000

A.  First time Setup:  Register a New Account

    - Enter an email and password to create a new account.

Afterwards you will automatically be logged in.

### 4. Run Locally (For Developers)

docker-compose --env-file .env up --build

## 🧪 API Endpoints

| Method | Endpoint  | Description                         |
| ------ | --------- | ----------------------------------- |
| GET    | `/menu`   | Returns QA/TA menu options          |
| POST   | `/select` | Selects assistant based on category |
| POST   | `/chat`   | Sends user message to MagDi         |

### Example Payload

{
  "user_id": "user123",
  "category": "qa_info",
  "message": "What is exploratory testing?"
}

## 📁 Project Structure (Simplified)

magdi-ai/
├── backend/
│   ├── app.py
│   ├── database.py
│   └── ...
├── frontend/
│   ├── src/
│   └── ...
├── .env
├── .env.prod
├── docker-compose.yml
├── Dockerfile (backend)
├── Dockerfile (frontend)
└── README.md

## 🔧 Tips

Run docker volume ls and docker volume rm to manage DB state during testing.

Use .env.prod.example as a template for production keys.

Logs are printed to stdout; use docker-compose logs to inspect.

Want to reset DB? Remove volume: docker volume rm magdi-ai-db-data

## 🧪 To inspect logs

docker-compose logs -f


## ℹ️ About and Versioning

MagDi AI v0.1.0 Alpha
For feedback or bugs, submit issues via GitHub.

## 📜 License

This project is licensed under the MIT License. See LICENSE for details.
```

## 🙏 Acknowledgements

- OpenAI for the Assistants API

- The open-source community ❤️

## ✨ Contributing

Fork, test, and send your PR! Contributions and ideas welcome as MagDi evolves.

---

Let me know if you’d like this saved to `README.md` or output as a downloadable file.








