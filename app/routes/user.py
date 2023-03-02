from fastapi import APIRouter, Depends
from models.users import User
from schemas.user import DisplayUser
from utils.database import get_db

router = APIRouter(prefix="/user")


@router.get("/{user_name}", response_model=DisplayUser)
def get_user_name(user_name, db_conn=Depends(get_db)):
    user = (
        db_conn.query(User.user_id, User.user_name, User.display_name)
        .filter(User.user_name == user_name.lower())
        .first()
    )
    return user
