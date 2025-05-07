# Task Manager API

Welcome to the **Task Manager API**!  
This is a simple REST API built with **FastAPI** for managing tasks.

---

## 🚀 Features
- View a welcome message at the root URL
- Fetch a list of sample tasks
- Built using FastAPI, a modern and high-performance web framework

---

## 🛠 Tech Stack
- **Python 3.9+**
- **FastAPI**
- **Uvicorn** (for running the server)

---

## 🧠 How to Run Locally

1. Clone the repository:

   git clone https://github.com/Jayant-Kaushik-Dev/task-manager-api.git
   cd task-manager-api

2. Create and activate a virtual environment

    python3 -m venv venv
    source venv/bin/activate  # On Mac/Linux

3. Install the dependencies:

    pip install fastapi uvicorn

4. Run the development server:

    uvicorn main:app --reload

5. Open your browser and visit:

    http://127.0.0.1:8000 to see the Welcome message

    http://127.0.0.1:8000/docs to explore interactive API documentation (thanks to Swagger UI)

