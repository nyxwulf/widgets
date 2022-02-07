from typing import Optional

from pydantic import BaseModel, Field
from pydantic.types import constr

class WidgetBase(BaseModel):
    name: constr(max_length=64) = Field(..., example="ZHEXBL4mmx10cm")
    description: Optional[constr(max_length=256)] = Field(None, example="Zinc Hex Bolts 4mm x 10cm")
    num_parts: int = Field(..., example=50)

class WidgetCreate(WidgetBase):
    pass

class Widget(WidgetBase):
    widget_id: int

    class Config:
        orm_mode = True
