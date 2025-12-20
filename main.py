from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predict import predict_category
from insights import generate_insights
from dotenv import load_dotenv
import os

load_dotenv()

PORT = int(os.getenv("PORT", 8000))
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(",")

app = FastAPI(title="Finance AI Service")

if "*" in ALLOWED_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["POST", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization"],
    )
else:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=False,
        allow_methods=["POST", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization"],
    )

class ExpenseRequest(BaseModel):
    description: str

class InsightRequest(BaseModel):
    summary: dict
    breakdown: list
    alerts: list

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ai/predict-category")
def predict(req: ExpenseRequest):
    category, confidence = predict_category(req.description)
    return {
        "category": category,
        "confidence": confidence
    }

@app.post("/ai/generate-insights")
def generate(req: InsightRequest):
    insights = generate_insights(req.summary, req.breakdown, req.alerts)
    return {
        "insights": insights
    }