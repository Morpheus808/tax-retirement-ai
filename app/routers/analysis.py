from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AnalysisRequest(BaseModel):
    age: int
    salary: float
    super_balance: float

@router.post("/")
def analyse_data(request: AnalysisRequest):
    """
    Basic analysis endpoint — later this will handle tax calculations,
    investment projections, and retirement modelling.
    """
    estimated_tax = request.salary * 0.30  # Simple placeholder
    projected_super = request.super_balance + (request.salary * 0.10)

    return {
        "ok": True,
        "message": "Analysis complete",
        "estimated_tax": estimated_tax,
        "projected_super": projected_super,
        "age": request.age,
    }
