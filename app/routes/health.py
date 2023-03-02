from fastapi import APIRouter

router = APIRouter(prefix="/health")


@router.get("/")
def health():
    return {"message": "Server is up and running"}
