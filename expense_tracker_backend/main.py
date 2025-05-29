from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from sqlmodel import Session, select
from database import init_db, get_session
from models import User, Expense
from schemas import UserCreate, ExpenseCreate
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )

@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)

@app.get("/")
async def root():
    return {"message": "Hello from Vercel API!", "status": "running"}

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    try:
        new_user = User(name=user.name, email=user.email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/", response_model=List[User])
async def get_users(session: Session = Depends(get_session)):
    try:
        return session.exec(select(User)).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Expense endpoints
@app.post("/expenses/", response_model=Expense)
async def create_expense(expense: ExpenseCreate, session: Session = Depends(get_session)):
    try:
        user = session.get(User, expense.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        new_expense = Expense(**expense.dict())
        session.add(new_expense)
        session.commit()
        session.refresh(new_expense)
        return new_expense
    except Exception as e:
        if "User not found" in str(e):
            raise e
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/expenses/", response_model=List[Expense])
async def get_expenses(session: Session = Depends(get_session)):
    try:
        return session.exec(select(Expense)).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/expenses/user/{user_id}", response_model=List[Expense])
async def get_expenses_by_user(user_id: int, session: Session = Depends(get_session)):
    try:
        return session.exec(select(Expense).where(Expense.user_id == user_id)).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def catch_all(request: Request, path: str):
    return {"message": f"Route {path} not found", "method": request.method}