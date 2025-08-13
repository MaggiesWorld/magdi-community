# 🤖 Magdi-AI – The AI Assistant for QA and Test Automation

Magdi-AI is a smart, OpenAI-powered assistant designed to streamline workflows for professionals in **Software Quality Assurance (QA)** and **Test Automation (TA)**. With features like intelligent query routing, persistent chat threads, and containerized deployment, MagDi helps teams get answers, generate documentation, and boost productivity.

🚀 **Now in Release REL.2.0.0.0 ** Try it locally or install as a PWA, SaaS or on your mobile device.

---

## 🚀 Features

- 🔍 **Agent Selection & Multi-Agent Interaction**
- ❓ **Answer Inquiries about QA and Automation**
- 📄 **Generate Software QA Documents**
- ✅ **Generate Test Cases**
- 📋 **Clipboard Copy for Easy Sharing**
- 🖥️ **Analyze Test Results**
- 💬 **Persistent Sessions & Threading**
- 🗃️ **PostgreSQL Integration**
- 🔒 **Environment Separation: Dev vs Prod**
- 🐳 **Dockerized Deployment**

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

### Docker Installation
Ensure you have Docker and Docker Compose installed on your machine:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- OpenAI API key
- Secret key for user auth (Flask)

### SaaS Version
- [MagDi SaaS](https://magdi-ai-frontend.fly.dev/) is available for use without setup. Just sign up and start using it!

This version provides complimentary access to the MagDi AI assistant with all features enabled.

---

## 🛠️ Docker Setup and Run

Bring your own OpenAI API key and secret key for user authentication.

### 1. Clone the Repository

```bash
git clone https://github.com/MaggiesWorld/magdi-community.git
cd magdi-community

### 2. Setup Environment Variables

A.  copy .env.example to .env.prod

B.  open .env.prod and update the following:

    i.  OPENAI_API_KEY=your_key_here
    ii. X_API_KEY=your_secret_key
    iii RATE_LIMIT_PER_USER=20 (Set to your desired daily token limit))

Note: The X_API_KEY is used for user authentication in the backend.
You can generate the secret using the command,

python -c "import secrets; print(secrets.token_hex(32))"

```

### Examples

Here are some example files that will help you get started using Magdi-AI

- [3-slot-casino-spec.txt](./examples/3-slot-casino-spec.txt) - A sample spec file for a 3-slot casino game.

Scenario: You can use this spec file to test the capabilities of MagDi AI in generating documents and test cases
1. Copy the spec file to your local machine.
2. Use the Magdi-AI assistant 'MagdiWriter' to generate a QA document based on the spec.
   Example command:
   - Upload the spec file and ask: "Generate QA/Testplan document for this spec"
   - Ask 'Create a comprehensive test plan for this spec'.

   Magdi will generate a QA test plan based on the spec.


- [3-slot-casino-testResults.json](./examples/3-slot-casino-testResults.json) - A sample test results file for the same game.

Scenario: You can use this test results file to test the capabilities of MagDi AI in analyzing test results.
1. Copy the test results file to your local machine.
2. Use the Magdi-AI assistant 'MagdiAnalyzer' to analyze the test results.
   Example command:
   - Upload the test results file and ask: "Analyze these test results"
   - Ask 'What are the key findings from these test results?'

   Magdi will analyze the test results and provide insights.

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

# Magdi AI Test Project

UI automation and backend testing for the Magdi AI platform.

## 🧪 API (v2)

### Endpoints

| Method | Path                       | Auth  | Content-Type                  | Notes                                                                                                                                     |
| ------ | -------------------------- | ----- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| GET    | `/menu`                    | —     | —                             | Returns starter menu/greeting.                                                                                                            |
| POST   | `/select`                  | —     | `application/json`            | Body: `user_id`, `category`. Returns `assistant_id`, starter message.                                                                     |
| POST   | `/start_conversation`      | —     | `application/json`            | Body: `user_id`, `assistant_id`, `category`, `agent_name`, `llm_model?`. Returns `conversation_id`.                                       |
| POST   | `/conversation/upload`     | —     | `multipart/form-data`         | Form fields: `files[]`, `user_id`, `conversation_id`. Saves files to convo.                                                               |
| POST   | `/chat`                    | —     | `multipart/form-data` **req** | Form fields: `user_id`, `category`, `message`, `conversation_id`, `llm_model?`, optional `files[]`. Uses latest uploaded file as context. |
| POST   | `/end_conversation`        | —     | `application/json`            | Body: `conversation_id`. Marks conversation completed.                                                                                    |
| GET    | `/config/rate-limit`       | —     | —                             | Returns daily token allowance.                                                                                                            |
| GET    | `/usage?user_id=...`       | —     | —                             | Returns usage count + limit.                                                                                                              |
| GET    | `/version`                 | —     | —                             | Returns `APP_INFO`.                                                                                                                       |
| GET    | `/metrics`                 | —     | —                             | Prometheus metrics.                                                                                                                       |
| GET    | `/metrics-update-visitors` | —     | —                             | Updates visitors gauge.                                                                                                                   |
| GET    | `/metrics-update-tokens`   | —     | —                             | Updates tokens gauge.                                                                                                                     |
| POST   | `/login`                   | —     | `application/json`            | Body: `email`, `password`.                                                                                                                |
| POST   | `/register`                | —     | `application/json`            | Body: `email`, `password`, `confirmPassword`.                                                                                             |
| GET    | `/validate-user`           | ✅ JWT | —                             | Query: `user_id`. Validates user exists.                                                                                                  |

> ⚠️ `/chat` now **requires** `multipart/form-data` even if no files are sent. Sending JSON will result in `400`.

---

### Typical Flow

#### 1) Select Agent

```bash
curl -X POST http://localhost:5000/select \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "category": "<valid-category>"
  }'
```

#### 2) Start Conversation

```bash
curl -X POST http://localhost:5000/start_conversation \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "assistant_id": "asst_xxx",
    "category": "<valid-category>",
    "agent_name": "<AgentName>",
    "llm_model": "gpt-4"
  }'
```

#### 3) Upload File (Optional)

```bash
curl -X POST http://localhost:5000/conversation/upload \
  -F "user_id=1" \
  -F "conversation_id=UUID" \
  -F "files=@./examples/sample.txt"
```

#### 4) Chat (Multipart Required)

```bash
curl -X POST http://localhost:5000/chat \
  -F "user_id=1" \
  -F "category=<valid-category>" \
  -F "message=What does the document contain?" \
  -F "conversation_id=UUID"
```

#### 5) End Conversation

```bash
curl -X POST http://localhost:5000/end_conversation \
  -H "Content-Type: application/json" \
  -d '{ "conversation_id": "UUID" }'
```

---

### Postman Form-Data for `/chat`

* **Text**: `user_id` = `1`
* **Text**: `category` = `<valid-category>`
* **Text**: `message` = `What does the document contain?`
* **Text**: `conversation_id` = `UUID`
* **Text** (optional): `llm_model` = `gpt-4`
* **File** (optional): `files[]` = *your file*

---

**Version:** REL.2.0.0.0

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
├── examples/
│   ├── 3-slot-casino-spec.txt
│   └── 3-slot-casino-testResults.txt


## 🔧 Tips

Run docker volume ls and docker volume rm to manage DB state during testing.

Use .env.prod.example as a template for production keys.

Logs are printed to stdout; use docker-compose logs to inspect.

Want to reset DB? Remove volume: docker volume rm magdi-ai-db-data

## 🧪 To inspect logs

docker-compose logs -f


## ℹ️ About and Versioning

Magdi-AI REL.2.0.0.0 
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

---

## ℹ️ About and Versioning

Magdi-AI REL.2.0.0.0

📬 Issues? Submit on GitHub or [send feedback](https://forms.gle/h5vuZMoiFyDgtHYe6)

---

## 💚 Support Magdi

If you find Magdi helpful and want to see it grow, please consider supporting the project:

- [☕ Buy Me a Coffee](https://github.com/sponsors/MaggiesWorld)
- [⭐ GitHub Sponsors](https://buymeacoffee.com/magdiai)
- [![Open Collective](https://opencollective.com/magdi-ai/tiers/backer/badge.svg?label=backer&color=brightgreen)](https://opencollective.com/magdi-ai)
- [![LibHunt](https://www.libhunt.com/r/magdi-community)](https://www.libhunt.com/r/magdi-community)


---

## 💼 Want a Hosted Version?

We're exploring a hosted version of Magdi — no setup required.

📧 [Register your interest](mailto:magdisolutions@gmail.com)

## 📜 License

This project is licensed under the MIT License. See LICENSE for details.

## 🙏 Acknowledgements

- OpenAI for the Assistants API
- The open-source community ❤️

## ✨ Contributing

Fork, test, and send your PR! Contributions and ideas welcome as MagDi evolves.







