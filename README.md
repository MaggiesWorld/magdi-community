# 🤖 Magdi-AI — The QA & Test Automation Assistant (REL 3.0.0.0)

Magdi-AI is an AI-powered multi-agent system designed to accelerate **QA**, **Test Automation**, and **Engineering Productivity**.

<<<<<<< HEAD
Release **3.0.0.0** introduces a unified **Test Generation Wizard**, a **Screen Scrape Engine**, and a new user-facing agent — **MagdiPartner** — focused on pair programming, test updates, and code refinement.

Magdi-AI helps teams:

- Generate new automation frameworks
- Update and refine existing automation projects
- Scrape and understand complex UIs
- Repair and improve failing automated tests
- Analyze test results
- Produce QA documentation
=======
🚀 **Now in Release REL.2.0.0.0 ** Try it locally or install as a PWA, SaaS or on your mobile device.
>>>>>>> 91785b2b9c795e57c7442077ffa36cc0d4c63261

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
cp .env.example .env.prod

Update the following values:
OPENAI_API_KEY=your_key_here
X_API_KEY=your_secret_here
RATE_LIMIT_PER_USER=20
MAGDI_WORK_DIR=your_work_directory_path

Generate a secure secret key:
python -c "import secrets; print(secrets.token_hex(32))"

<<<<<<< HEAD
Run in Developer Mode:
=======
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

>>>>>>> 91785b2b9c795e57c7442077ffa36cc0d4c63261
docker-compose --env-file .env up --build

Application will be available at:
http://localhost:3000

Run in Production Mode:
docker-compose --env-file .env.prod -f docker-compose.prod.yml up


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
