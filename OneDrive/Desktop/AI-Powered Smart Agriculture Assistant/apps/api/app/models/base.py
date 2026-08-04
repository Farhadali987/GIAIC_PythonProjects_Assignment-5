from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from app.database.session import Base

class TimestampMixin:
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    is_deleted = Column(Integer, default=0, nullable=False) # 0 for false, 1 for true (soft delete)
