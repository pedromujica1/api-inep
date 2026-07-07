from fastapi import APIRouter


router = APIRouter(prefix="/api/debug", tags=["debug"])


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
