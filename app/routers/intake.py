from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()

class IntakeData(BaseModel):
    name: str
    age: int = Field(..., ge=18, le=75)
    salary: float
    super_balance: float

@router.post("/")
def collect_user_data(data: IntakeData):
    """
    Intake endpoint — collects user info and returns acknowledgment.
    """
    return {
        "ok": True,
        "message": f"Data received for {data.name}",
        "age": data.age,
        "salary": data.salary,
        "super_balance": data.super_balance,
    }
