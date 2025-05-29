🧾 Expense Tracker App
A full-stack expense tracker application built with FastAPI on the backend and React on the frontend.

📁 Project Structure
expense-tracker/
├── expense_tracker_backend/ # FastAPI backend
├── frontend/ # React frontend
└── README.md # Project documentation

🚀 Getting Started

Clone the Repository
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker

⚙️ Backend Setup (FastAPI)
📂 Navigate to Backend Directory
cd expense_tracker_backend

📦 Install Requirements
Create a virtual environment (recommended):
python -m venv venv

Activate the virtual environment:

On macOS/Linux:
source venv/bin/activate

On Windows:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

▶️ Run the Server
uvicorn main:app --reload
The backend will be available at: http://127.0.0.1:8000

📚 API Documentation
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

🌐 Frontend Setup (React)
📂 Navigate to Frontend Directory
cd ../frontend

📦 Install Dependencies
npm install

▶️ Run the React App
npm start
The frontend will be available at: http://localhost:3000

📝 Additional Notes
Make sure you have Python 3.7+ and Node.js installed

The backend requires an active virtual environment for dependency isolation

The --reload flag enables hot-reloading for development