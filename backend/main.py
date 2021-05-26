from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api.api import api_router
from config.config import settings
import uvicorn


app = FastAPI(
    debug=True,
    title=settings.APP_NAME, openapi_url=f"{settings.API_STR}/openapi.json"
)

origins = ['*']

app.include_router(api_router, prefix=settings.API_STR)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )