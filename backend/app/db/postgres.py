from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

POSTGRES_URL = os.getenv("DATABASE_URL")

engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(bind=engine)
