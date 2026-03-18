from fastapi import FastAPI
from app.routes.analyze import router
from app.core.rate_limiter import limiter
from slowapi.middleware import SlowAPIMiddleware
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://trade-opportunities-analyzer.vercel.app",
]

app = FastAPI(title="Trade Opportunities API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(router)