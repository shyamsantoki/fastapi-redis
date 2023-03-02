from pydantic import BaseModel


class DisplayUser(BaseModel):
    user_id: str
    user_name: str
    display_name: str

    class Config:
        orm_mode = True
