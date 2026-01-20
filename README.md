
---

# 📘 `finance-ai-services`

```md
# FinanceAI AI Service

AI microservice for FinanceAI responsible for transaction categorization
and insight generation.

## Tech Stack
- Python
- FastAPI
- Rule-based NLP
- Uvicorn

## Features
- Transaction category prediction using keyword scoring
- Confidence-based classification
- Income vs expense detection support
- AI insights generation based on spending patterns
- Health endpoint for cold-start warm-up

## Design Highlights
- Case-insensitive & normalized text matching
- Strong vs weak keyword scoring system
- Safe fallback when no confident category is found
- Stateless & independently deployable service

## API Endpoints
- `GET /health`
- `POST /predict-category`
- `POST /generate-insights`

## Example Payload
{
  "description": "Swiggy Order"
}
