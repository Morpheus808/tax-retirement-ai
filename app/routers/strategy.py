from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()

class StrategyInput(BaseModel):
    age: int = Field(..., ge=18, le=75)
    salary: float
    super_balance: float
    member_concessional: float = 0.0  # already sacrificing/CCs

@router.post("/")
def recommend_strategy(inp: StrategyInput):
    """
    Minimal placeholder strategy.
    We’ll replace with AU tax + super logic next.
    """
    # toy suggestion: salary sacrifice 5% of salary (capped later)
    suggested_ss = round(inp.salary * 0.05, 2)
    return {
        "ok": True,
        "suggested_salary_sacrifice": suggested_ss,
        "notes": "Placeholder only. Real AU logic coming next."
    }
