# 🤖 AgenticAI — Stage 11: Production Multi-Agent System

> Built by **Tahir Hussain** — AI Engineer in training | Python · FastAPI · Docker · Kubernetes  
> 📍 Pakistan · 🌍 Open to Remote

---

## 🚀 What This Project Does

A **production-grade multi-agent AI system** built from scratch using Python and local LLMs (no paid APIs ever).

This is **Stage 11 of an 11-stage AI Engineering roadmap** — covering everything from basic agents to full Kubernetes deployment.

The system runs multiple specialized AI agents behind a FastAPI server, with real-time task routing, guardrails, canary releases, Docker containerization, and Kubernetes orchestration.

---

## 🏗️ Architecture

```
Client Request
      │
      ▼
FastAPI Server (main.py)
      │
      ├── Guardrail Filter  ──► blocks harmful inputs
      │
      ├── Canary Router  ──► 10% traffic → canary agent
      │
      ├── Task Queue (async)
      │
      └── Multi-Agent Pipeline
            ├── Agent 1 — Primary reasoning
            ├── Agent 2 — Specialist task
            └── Agent 3 — Response synthesis
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.11 |
| **API Server** | FastAPI + Uvicorn |
| **LLM** | Ollama llama3.1 (local, GTX 1660 6GB) |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes (kubectl) |
| **CI/CD** | GitHub Actions |
| **Release Strategy** | Canary deployments (10% routing) |
| **Logging** | Custom logger.py |

---

## ✅ Features Built

- 🤖 **Multi-agent pipeline** — specialized agents working in sequence
- 🛡️ **Guardrail filter** — blocks harmful/invalid inputs before processing
- ⚡ **Async task queue** — non-blocking request handling
- 🐳 **Dockerized** — fully containerized, runs anywhere
- ☸️ **Kubernetes deployment** — deployed with `deployment.yaml`, verified running
- 🔁 **Canary releases** — 10% traffic routed to new version for safe rollouts
- ↩️ **Rollback strategy** — instant rollback script tested and working
- 🔄 **CI/CD pipeline** — GitHub Actions auto-builds and tests on every push
- 🏥 **Health endpoints** — `/health` for container and Kubernetes readiness checks
- 🌐 **Web UI** — basic HTML interface (`userInterface.html`)

---

## 📁 Project Structure

```
stage11/
├── main.py                 # FastAPI app entry point
├── config.py               # App configuration
├── logger.py               # Logging setup
├── graceful_shutdown.py    # Clean shutdown handler
├── task_queue.py           # Async task queue
├── worker.py               # Background worker
├── canary_config.py        # Canary release config
├── rollback.py             # Rollback strategy
├── userInterface.html      # Web UI
├── Dockerfile              # Container definition
├── deployment.yaml         # Kubernetes deployment + service
├── agents/                 # Agent modules
├── models/                 # Data models
├── routers/                # FastAPI route handlers
└── .github/workflows/      # CI/CD GitHub Actions
```

---

## 🚀 Run Locally

**Prerequisites:** Python 3.11, Ollama installed, llama3.1 pulled

```bash
# Clone the repo
git clone https://github.com/tahirAliicodes/AgenticAI-Stage11.git
cd AgenticAI-Stage11

# Activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements-docker.txt

# Start the server
uvicorn main:app --reload --port 8000
```

Visit: `http://localhost:8000/docs`

---

## 🐳 Run with Docker

```bash
docker build -t stage11-app .
docker run -p 8000:8000 stage11-app
```

---

## ☸️ Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
kubectl get pods
kubectl port-forward service/stage11-service 8000:8000
```

---

## 🔄 CI/CD Pipeline

Every push to `main` triggers GitHub Actions:
1. ✅ Checkout code
2. ✅ Install dependencies
3. ✅ Run tests
4. ✅ Build Docker image

Every push to `canary` branch deploys the canary version.

---

## 📚 Full AI Engineer Roadmap (Stages 1–11)

| Stage | Topic | Status |
|---|---|---|
| 1 | Python + AI Basics | ✅ |
| 2 | Prompt Engineering | ✅ |
| 3 | Local LLMs with Ollama | ✅ |
| 4 | Agent Foundations | ✅ |
| 5 | Memory & Context | ✅ |
| 6 | Multi-Agent Systems | ✅ |
| 7 | FastAPI + REST APIs | ✅ |
| 8 | Computer Vision Integration | ✅ |
| 9 | Observability & Logging | ✅ |
| 10 | Security & Guardrails | ✅ |
| 11 | Docker + Kubernetes + CI/CD | ✅ **← You are here** |

---

## 👨‍💻 About Me

**Tahir Hussain** — CS graduate from Shah Abdul Latif University, Pakistan.

I build AI systems from scratch — no paid APIs, no shortcuts. Everything runs locally on a GTX 1660 6GB.

- 🎓 BS Computer Science (2024)
- 🔬 Final Year Project: YOLOv8 real-time object detection — 40% latency reduction
- 📱 Flutter mobile apps — freelance, full project lifecycle
- 🤖 11 stages of Agentic AI — self-taught, documented, shipped

📧 alitahir629@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/tahir-hussain-5427772b9)  
💻 [GitHub](https://github.com/tahirAliicodes)

---

> ⭐ If this project helped you, consider giving it a star!
