# 🚀 Getting Started

## Requirements

- Docker Desktop (Windows/Mac) or Docker Engine (Linux)
- Git

---

## Install

```bash
git clone https://github.com/MaggiesWorld/magdi-community.git
cd magdi-community

### Run installer:

Windows:
install.magdi-ai.bat

Mac/Linux:
chmod +x install.magdi-ai.sh
./install.magdi-ai.sh

```

### Configure Environment

Update .env:
OPENAI_API_KEY=your_key
X_API_KEY=your_secret
SECRET_KEY=REPLACE-ME-H256 openssl rand -hex 32
JWT_SECRET_KEY=Replace Me with python -c "import secrets; print(secrets.token_hex(32))"
MAGDI_WORK_DIR=./magdi-runs

### Run Application
http://localhost:3000

## First Workflow
Open Test Generation Wizard (MagdiCreator)
Provide input (intructions, File, URL)
Select settings (tool, framework, language)
Generate project
Follow instructions to execute tests



