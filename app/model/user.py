from app.repository.db import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(256), unique=True, nullable=False)
    password = Column(String(256), nullable=False)