from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from src.plot import plot_data
from src.types import PlotData

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/plot")
async def plot(data: PlotData):
    try:
        image_path = plot_data(data)
        return FileResponse(path=image_path, media_type="image/png")
    except Exception as e:
        print(e)
        return { "error": "Whoops, something bad happened"}

