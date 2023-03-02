from sqlalchemy import Column, Date, ForeignKey, Integer, String

from app.models import Base
from app.models.users import User


class Tweet(Base):
    __tablename__ = "tweets"
    tweet_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey(User.user_id), nullable=False)
    tweet_url = Column(String)
    date = Column(Date)
    content = Column(String)
    reply_count = Column(Integer)
    retweet_count = Column(Integer)
    like_count = Column(Integer)
    quote_count = Column(Integer)
    source_label = Column(String)
    lang = Column(String)
    links_in_content = Column(String)
    media = Column(String)
    retweeted_tweet = Column(String)
    quoted_tweet = Column(String)
    in_reply_to_tweet_id = Column(String)
    mentioned_users = Column(String)
    hashtags = Column(String)
    view_count = Column(Integer)
    embed_link = Column(String)
    tweet_scraped_date = Column(Date, nullable=False)
    zeroshot_filtering = Column(String)
    category = Column(String)
    sub_category = Column(String)
    filters_category = Column(String)
    zeroshot_filtering_category = Column(String)
