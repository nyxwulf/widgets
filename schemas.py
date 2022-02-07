from typing import Optional

from datetime import datetime

from pydantic import BaseModel, Field
from pydantic.types import constr

class WidgetBase(BaseModel):
    name: constr(max_length=64) = Field(..., example="ZHEXBL4mmx10cm")
    description: Optional[constr(max_length=256)] = \
        Field(None, example="Zinc Hex Bolts 4mm x 10cm")
    num_parts: int = Field(..., example=50)

class WidgetCreate(WidgetBase):
    pass

class WidgetUpdate(BaseModel):
    widget_id: int
    name: Optional[constr(max_length=64)] = Field(None, example="GHEXBL4mmx10cm")
    description: Optional[constr(max_length=256)] = \
        Field(None, example="Galvanized Hex Bolts 4mm x 10cm")
    num_parts: Optional[int] = Field(None, example=50)

class Widget(WidgetBase):
    widget_id: int

    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
