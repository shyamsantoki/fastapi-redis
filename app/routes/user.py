import redis
from fastapi import APIRouter, Depends
from models.users import User
from schemas.user import DisplayUser
from utils.database import get_db
from utils.units import HOUR

router = APIRouter(prefix="/user")


@router.get("/{user_name}", response_model=DisplayUser)
def get_user_name(user_name, db_conn=Depends(get_db)):
    conn = redis.Redis("localhost")
    redis_user_name = f"user::{user_name}"
    redis_data = conn.hgetall(redis_user_name)
    if redis_data == {}:
        user = db_conn.query(User).filter(User.user_name == user_name.lower()).first()
        pydantic_fields = DisplayUser.schema().get("properties").keys()
        data_to_cache = {key: getattr(user, key) for key in pydantic_fields}
        conn.hmset(redis_user_name, data_to_cache)
        conn.expire(redis_user_name, 1 * HOUR)
    else:
        user = {
            key.decode("ascii"): user.get(key).decode("ascii")
            for key in redis_data.keys()
        }
        user = DisplayUser.parse_obj(user)
    return user
