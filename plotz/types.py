from pydantic import BaseModel
from enum import Enum
from typing import Optional

"""
{
  title: string;
  x-label?: string;
  y-label?: string;
  values: {label: string; value: number}[];
  type: enum(stacked, bar, pie);
}
"""

class PlotType(str, Enum):
    bar = "bar"
    pie = "pie"
    stacked = "stacked"

class PlotValues(BaseModel):
    label: str
    value: float

class PlotData(BaseModel):
    title: str
    x_label: Optional[str] = None
    y_label: Optional[str] = None
    values: list[PlotValues] = []
    type: PlotType

