from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from db.db import Base


class Entity(Base):
    __tablename__ = "entity"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)
