from fastapi import APIRouter, Depends, HTTPException, Request, Path
from fastapi.responses import Response
from app.services.scraper import fetch_news
from app.services.ai_service import analyze_data
from app.services.report import generate_markdown
from app.core.security import verify_token
from app.core.rate_limiter import limiter
from app.core.session_store import track_request
from app.utils.logger import logger

router = APIRouter()


def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    token = auth_header.split(" ")[1]
    user = verify_token(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return user


@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,
    sector: str = Path(..., min_length=3, max_length=50, pattern="^[a-zA-Z ]+$"),
    user=Depends(get_current_user)
):
    logger.info(f"User {user['sub']} requested analysis for {sector}")

    track_request(user["sub"])

    try:
        news = await fetch_news(sector)
    except Exception as e:
        logger.error(f"Scraper error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch market data")

    try:
        analysis = await analyze_data(sector, news)
    except Exception as e:
        logger.error(f"AI error: {str(e)}")
        raise HTTPException(status_code=500, detail="AI analysis failed")

    report = generate_markdown(sector, analysis)

    return Response(
        content=report,
        media_type="text/markdown; charset=utf-8",
        headers={
            "Content-Disposition": f"attachment; filename={sector}_report.md"
        }
    )