#!/bin/bash

echo "=========================================="
echo "Magdi-AI Installer (Linux/Mac)"
echo "=========================================="

# --- Check Docker ---
if ! docker info > /dev/null 2>&1; then
  echo ""
  echo "ERROR: Docker is not running."
  echo "Please start Docker and try again."
  exit 1
fi

# --- Ensure .env exists ---
if [ ! -f ".env" ]; then
  echo "Creating .env from .env.example..."
  cp .env.example .env
  echo ""
  echo "WARNING: Please update the .env file with your API keys and settings."
  read -p "Press Enter to continue once ready..."
fi

# --- Check port 3000 ---
if lsof -i :3000 > /dev/null 2>&1; then
  echo ""
  echo "ERROR: Port 3000 is already in use."
  echo "Please stop the application using port 3000 and try again."
  exit 1
fi

echo ""
echo "=========================================="
echo "Stopping existing Magdi-AI containers..."
echo "=========================================="
docker compose down > /dev/null 2>&1

echo ""
echo "=========================================="
echo "Starting Magdi-AI..."
echo "=========================================="
docker compose up -d

if [ $? -ne 0 ]; then
  echo ""
  echo "ERROR: Failed to start containers."
  exit 1
fi

echo ""
echo "=========================================="
echo "SUCCESS: Magdi-AI is running!"
echo "Open: http://localhost:3000"
echo "=========================================="