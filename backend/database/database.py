from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config.config import settings

print(settings.SQLALCHEMY_DATABASE_URL)
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, connect_args={"options": "-c timezone=gmt+3"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)