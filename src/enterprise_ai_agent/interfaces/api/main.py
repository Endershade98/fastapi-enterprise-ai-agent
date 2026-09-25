# src/enterprise_ai_agent/interfaces/api/main.py

from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Agent & LLMOps Gateway",
    version="0.1.0",
)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

