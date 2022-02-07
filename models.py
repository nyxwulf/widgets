from sqlalchemy import Column, Integer, String

from database import Base


class Widget(Base):
    __tablename__ = "WIDGETS"

    widget_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    num_parts = Column(Integer)


