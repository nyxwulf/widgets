from sqlalchemy import Column, DateTime, Integer, String

from database import Base


class Widget(Base):
    __tablename__ = "WIDGETS"

    widget_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), index=True)
    description = Column(String(256))
    num_parts = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


