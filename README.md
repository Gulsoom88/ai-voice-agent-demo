# 📞 AI Voice Agent Dashboard – Demo Version

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.26.0-orange?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/Gulsoom88/ai-voice-agent-demo)](https://github.com/Gulsoom88/ai-voice-agent-demo/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/Gulsoom88/ai-voice-agent-demo)](https://github.com/Gulsoom88/ai-voice-agent-demo/issues)

---

## 🎯 Project Summary

**AI Voice Agent Dashboard** is a demo web-based control panel that allows users to **connect, monitor, and manage AI-powered voice agents** from external platforms such as Retell.ai, Vapi.ai, ElevenLabs, or Voiceflow.

The demo focuses on **integration and visualization**, not building agents from scratch. Users can:  
- Trigger outbound calls from incoming leads  
- Track call status in real time  
- Manage queues with retry logic  
- Log call outcomes

This serves as a **proof-of-concept for a future scalable SaaS platform**.

---

## 🛠 Demo Goals

- Connect and simulate an external voice agent via API  
- Trigger calls based on leads (from Google Sheets or email parsers)  
- Display live call statuses and outcomes  
- Implement queue logic and retries for failed calls  
- Provide a user-friendly admin panel and dashboard

---

## 🔧 Key Features

- Connect to simulated Retell.ai or Vapi.ai agents  
- Display agent status (Active / Offline / Error)  
- Receive leads from **Google Sheets** or **email parsers**  
- Trigger outbound calls (simulated for demo)  
- Queue calls using **FIFO** logic with retry for failures  
- Log calls with name, number, status, duration, timestamp  
- Real-time dashboard updates without manual refresh  
- Simple admin panel for manual test triggers

---

## 🏗 Architecture

![Architecture Diagram](assets/architecture_diagram.png)

- **Backend:** FastAPI for lead management and queue logic  
- **Database:** SQLite (or Supabase) for lead storage  
- **Frontend:** Streamlit for live dashboard and admin panel  
- **Lead Sources:** Google Sheets, email parser  
- **Call Simulation:** Python-based queue with retry logic  
- **Security:** API keys stored securely in backend; only dummy/test data used

---

## 📸 Screenshots

### Dashboard Main View
![Dashboard](assets/dashboard_main.png)

### Backend Leads Endpoint
![Backend Leads](assets/backend_terminal.png)

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Gulsoom88/ai-voice-agent-demo.git
cd ai-voice-agent-demo
