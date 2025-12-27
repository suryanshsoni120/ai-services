from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
from predict import predict_category
from insights import generate_insights
import os

origins = os.getenv("ALLOWED_ORIGINS")
origins = origins.split(",") if origins else ["*"]

app = FastAPI(title="Finance AI Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

class ExpenseRequest(BaseModel):
    description: str

class BreakdownItem(BaseModel):
    category: str
    total: float

class AlertItem(BaseModel):
    type: str
    category: Optional[str] = None

class InsightRequest(BaseModel):
    summary: Dict[str, float]
    breakdown: List[BreakdownItem]
    alerts: List[AlertItem]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ai/predict-category")
def predict(req: ExpenseRequest):
    return predict_category(req.description)

@app.post("/ai/generate-insights")
def generate(req: InsightRequest):
    if len(req.breakdown) > 10 or len(req.alerts) > 10:
        return {"insights": ["Data too large to analyze."]}

    insights = generate_insights(
        req.summary,
        req.breakdown,
        req.alerts
    )
    return {"insights": insights}