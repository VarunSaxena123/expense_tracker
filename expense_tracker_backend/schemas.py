from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    date: str
    category: str
    user_id: int
