# Finance AI Service

FastAPI-based AI microservice for:
- Expense category prediction
- Financial insights generation

## Tech Stack
- Python
- FastAPI
- Deployed on Render

## Endpoints
- POST /ai/predict-category
- POST /ai/insights
- GET /health

## Local Setup
pip install -r requirements.txt
uvicorn main:app --reload
