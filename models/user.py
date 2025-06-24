from sqlalchemy import Column, Integer, String
from backend.config.db import Base

class User(Base):
    __tablename__ = "tb_user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)