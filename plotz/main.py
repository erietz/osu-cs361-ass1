from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from starlette.background import BackgroundTask

from .plot import plot_data, remove_tmp_image
from .types import PlotData

app = FastAPI()

@app.post("/api/plot", response_class=FileResponse)
async def plot(data: PlotData):
    image_path = plot_data(data)
    return FileResponse(
            path=image_path,
            media_type="image/png",
            background=BackgroundTask(remove_tmp_image)
            )
