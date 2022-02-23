from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from enum import IntEnum



app = FastAPI()

"""
{
  title: string;
  x-label?: string;
  y-label?: string;
  values: {label: string; value: number}[];
  type: enum(stacked, bar, pie);
}
"""

class PlotType(IntEnum):
    stacked = 0
    bar = 1
    pie = 2

class PlotValues(BaseModel):
    label: str
    value: float

class PlotData(BaseModel):
    title: str
    x_label: Optional[str] = None
    y_label: Optional[str] = None
    values: list[PlotValues] = []
    type: PlotType


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/api/plot")
async def plot(data: PlotData):
    return data

