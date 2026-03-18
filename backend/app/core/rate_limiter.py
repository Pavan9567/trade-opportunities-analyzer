from slowapi import Limiter
from fastapi import Request

def user_rate_limit(request: Request):
    return request.headers.get("Authorization", "anonymous")

limiter = Limiter(key_func=user_rate_limit)