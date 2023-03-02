from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.configs.database import SQLALCHEMY_URL

engine = create_engine(SQLALCHEMY_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
