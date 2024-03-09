from fastapi import FastAPI
import uvicorn
from src.api.index import api_router

app = FastAPI(docs_url="/api-docs", openapi_url="/open-api-docs")

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

