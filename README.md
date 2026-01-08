# 📞 AI Voice Agent Dashboard

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.26.0-orange?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

---

This project is a fully functional **AI Voice Agent Dashboard** built with **FastAPI** and **Streamlit**. It allows you to manage, queue, and simulate calls to leads.

---

## 🖥️ Dashboard Features

- Live auto-refresh every few seconds
- View all leads and their statuses
- Call next lead simulation
- Color-coded lead status: Pending, Called, Failed
- Call timeline visualization

---

## 🛠️ Architecture

![Architecture Diagram](assets/architecture_diagram.png)

- **FastAPI backend** for handling leads
- **SQLite database** to store lead information
- **Streamlit frontend** for the dashboard
- In-memory queue to simulate live calls

---

## 📸 Screenshots

### Dashboard Main View
![Dashboard](assets/dashboard_main.png)

### Backend Leads Endpoint (Terminal)
![Backend Leads](assets/backend_terminal.png)

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Gulsoom88/ai-voice-agent-demo.git
cd ai-voice-agent-demo
