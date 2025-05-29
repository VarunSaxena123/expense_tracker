# 🧾 Expense Tracker App

A full-stack expense tracker application built with **FastAPI** on the backend and **React** on the frontend.

---

## 📁 Project Structure

expense-tracker/
├── expense_tracker_backend/ # FastAPI backend
├── frontend/ # React frontend
└── README.md # This file

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
⚙️ Backend Setup (FastAPI)
📂 Navigate to Backend
bash
Copy
Edit
cd expense_tracker_backend
📦 Install Requirements
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Run the Server
bash
Copy
Edit
uvicorn main:app --reload
The backend will be available at: http://127.0.0.1:8000

📚 API Docs
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

🌐 Frontend Setup (React)
📂 Navigate to Frontend
bash
Copy
Edit
cd ../frontend
📦 Install Dependencies
bash
Copy
Edit
npm install
▶️ Run the React App
bash
Copy
Edit
npm start
The frontend will be available at: http://localhost:3000

