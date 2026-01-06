# 🤖 Magdi-AI — The QA & Test Automation Assistant (REL 3.0.0.0)

Magdi-AI is an AI-powered multi-agent system designed to accelerate **QA**, **Test Automation**, and **Engineering Productivity**.

Release **3.0.0.0** introduces a unified **Test Generation Wizard**, a **Screen Scrape Engine**, and a new user-facing agent — **MagdiPartner** — focused on pair programming, test updates, and code refinement.

Magdi-AI helps teams:

- Generate new automation frameworks
- Update and refine existing automation projects
- Scrape and understand complex UIs
- Repair and improve failing automated tests
- Analyze test results
- Produce QA documentation

---

## 📜 License

Magdi-AI Community Edition is released under the **MIT License**.

You are free to:

- Use
- Modify
- Distribute
- Self-host

Under the terms of the MIT License.

See the `LICENSE` file in this repository for full details.


## 🚀 Key Features (REL 3.0)

### 🧙 Test Generation Wizard

Create **new** or **updated** test projects using:

- Pasted text
- Uploaded documents
- URLs
- Screen Scrape (Depth-based crawling)

Supports:
- Manual tests
- Automated tests
- Playwright (TS / JS / Python)
- Cypress
- Java-based frameworks

Wizard supports both **project creation** and **project update** flows.

---

### 🕷️ Screen Scrape Engine

Capture and analyze UI structure agnostically using **screen depth**:

- DOM structure
- Selectors
- Forms, buttons, dialogs
- Cross-page traversal
- Depth-controlled crawling to avoid over-scraping

Screen Scrape output feeds directly into Test Generation and Update workflows.

---

### 🧑‍🤝‍🧑 MagdiPartner — Pair Programming & Test Update Agent

**MagdiPartner** is the primary **user-facing agent** for:

- Updating existing test projects
- Refining generated tests
- Pair programming with the user
- Reviewing and improving code
- Diagnosing failing tests

MagdiPartner can:

- Explain failures and root causes
- Propose minimal patches or full file updates
- Improve selectors and flows
- Regenerate tests interactively with the user

> ℹ️ Internally, Magdi-AI uses specialized sub-agents to perform update operations. These are not user-facing and are orchestrated automatically by the system.

---

### 📄 Documentation & QA Output

Generate:

- Test Plans
- Test Cases
- Acceptance Criteria
- QA Checklists
- Analysis of test result files

---

## 🧱 Tech Stack

- **Frontend:** React + Vite + TailwindCSS
- **Backend:** Python (Flask) + Gunicorn
- **AI:** OpenAI Assistants API (multi-agent orchestration)
- **Database:** PostgreSQL
- **Containerization:** Docker + Docker Compose

---

## ⚙️ Running Magdi-AI Locally

### 1️⃣ Clone the Repository

git clone https://github.com/MaggiesWorld/magdi-community.git
cd magdi-community


## Environment Setup

Copy the example environment file:
cp .env.example .env

Update the following values:
OPENAI_API_KEY=your_key_here
X_API_KEY=your_secret_here
RATE_LIMIT_PER_USER=20
MAGDI_HOST_WORK_DIR=your_work_directory_path

Generate a secure secret key:
python -c "import secrets; print(secrets.token_hex(32))"

Run in Developer Mode:
docker-compose --env-file .env up --build

Application will be available at:
http://localhost:3000

Run in Production Mode:
docker-compose --env-file .env -f docker-compose.yml up


## 🧪 Test Project (Automation Suite)

The repository includes a Playwright automation suite covering:

- Authentication
- Chat UI
- Test Generation Wizard
- Screen Scrape flows
- Project update scenarios

Run all tests:
npx playwright test

Run a single test:
npx playwright test tests/01-login.test.ts

Run with browser UI:
npx playwright test --headed


## 🧩 API Overview (Backend)

### Core Conversation & Agent APIs

- `GET  /menu`  
  Returns starter menu / greeting.

- `POST /select`  
  Selects an agent category and returns assistant metadata.

- `POST /start_conversation`  
  Starts a new persistent conversation thread.

- `POST /conversation/upload`  
  Upload files into an active conversation context.

- `POST /chat`  
  Sends a user message to the active agent.

  ⚠️ **Important:**  
  This endpoint **requires `multipart/form-data`**, even when no files are sent.  
  Sending JSON will return `400 Bad Request`.

- `POST /end_conversation`  
  Gracefully closes a conversation thread.

---

### Project & Artifact APIs

- `GET /api/download?zip_id=<id>&disposable=1`  
  Downloads a generated or updated project ZIP.

  - `zip_id` maps to a generated artifact
  - `disposable=1` deletes the ZIP after download
  - Used by both **create** and **update** project flows

---

### Authentication & User APIs

- `POST /login`  
  Authenticates a user.

- `POST /register`  
  Registers a new user account.

- `GET  /validate-user`  
  Validates an authenticated user session (JWT-based).

---

### System & Metrics APIs

- `GET /version`  
  Returns backend application version info.

- `GET /config/rate-limit`  
  Returns daily token usage limits.

- `GET /usage?user_id=<id>`  
  Returns current token usage for a user.

- `GET /metrics`  
  Prometheus-compatible metrics endpoint.

- `GET /metrics-update-visitors`  
  Updates visitor gauge.

- `GET /metrics-update-tokens`  
  Updates token usage gauge.



## 🧭 Project Structure (Simplified)

magdi-ai/
├── backend/
│   ├── app.py
│   ├── assistants/
│   ├── routes/
│   └── ...
├── frontend/
│   ├── src/
│   └── ...
├── tests/            # Playwright automation
├── examples/         # Sample specs & test results
├── docker-compose.yml
├── docker-compose.prod.yml
└── README.md

## 📜 Version

Magdi-AI REL 3.0.0.0

## 🙏 Acknowledgements

- OpenAI Assistants API
- Docker
- The open-source community ❤️

## ✨ Contributing

Fork → Improve → Submit a PR.
Feedback and ideas are always welcome.

## 💚 Support Magdi-AI

If Magdi-AI helps you, consider supporting the project:

- ☕ Buy Me a Coffee
- ⭐ GitHub Sponsors
- Open Collective
- LibHunt
