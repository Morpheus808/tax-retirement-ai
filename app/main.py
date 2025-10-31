from fastapi import FastAPI
from app.routers import intake, analysis, strategy, report

app = FastAPI(title="Tax-Effective Retirement Strategies (AU)", version="0.1.0")

app.include_router(intake.router, prefix="/intake", tags=["intake"])
app.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
app.include_router(strategy.router, prefix="/strategy", tags=["strategy"])
app.include_router(report.router, prefix="/report", tags=["report"])

@app.get("/")
def root():
    return {"ok": True, "service": "tax-retirement-ai", "version": "0.1.0"}
