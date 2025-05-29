from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/users/", response_model=User)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    new_user = User(name=user.name, email=user.email)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@app.get("/users/", response_model=List[User])
def get_users(session: Session = Depends(get_session)):
    return session.exec(select(User)).all()

@app.post("/expenses/", response_model=Expense)
def create_expense(expense: ExpenseCreate, session: Session = Depends(get_session)):
    user = session.get(User, expense.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_expense = Expense(**expense.dict())
    session.add(new_expense)
    session.commit()
    session.refresh(new_expense)
    return new_expense

@app.get("/expenses/", response_model=List[Expense])
def get_expenses(session: Session = Depends(get_session)):
    return session.exec(select(Expense)).all()

@app.get("/expenses/user/{user_id}", response_model=List[Expense])
def get_expenses_by_user(user_id: int, session: Session = Depends(get_session)):
    return session.exec(select(Expense).where(Expense.user_id == user_id)).all()
