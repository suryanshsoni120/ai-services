from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predict import predict_category
from insights import generate_insights
from dotenv import load_dotenv
import os

load_dotenv()

PORT = int(os.getenv("PORT", 8000))
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app = FastAPI(title="Finance AI Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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
    try:
        result = predict_category(req.description)
        return result
    except Exception as e:
        return {
            "error": str(e)
        }

@app.post("/ai/generate-insights")
def generate(req: InsightRequest):
    try:
        insights = generate_insights(req.summary, req.breakdown, req.alerts)
        return {"insights": insights}
    except Exception as e:
        return {"error": str(e)}