from models import Base
from sqlalchemy import Boolean, Column, Date, Integer, String


class User(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key=True)
    user_name = Column(String)
    display_name = Column(String)
    description = Column(String)
    verified = Column(Boolean)
    created = Column(Date)
    followers_count = Column(Integer)
    friends_count = Column(Integer)
    statuses_count = Column(Integer)
    favourites_count = Column(Integer)
    listed_count = Column(Integer)
    media_count = Column(Integer)
    location = Column(String)
    protected = Column(Integer)
    description_link = Column(String)
    profile_image_url = Column(String)
    profile_banner_url = Column(String)
    tweet_scraped_date = Column(Date)
