from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

DATABASE_URL = "postgresql://destinpq_user:destinpq_user_1234@localhost:5432/video_gen"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
