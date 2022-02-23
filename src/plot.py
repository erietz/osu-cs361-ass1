from matplotlib import pyplot as plt
from pathlib import Path
from src.types import PlotData, PlotType
from datetime import datetime

def get_time_stamp() -> str:
    return datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

def plot_data(data: PlotData) -> Path:
    now = get_time_stamp()
    if data.type == PlotType.pie.value:
        return plot_pie(data, now)
    elif data.type == PlotType.bar.value:
        return plot_bar(data, now)
    elif data.type == PlotType.stacked.value:
        return plot_stacked(data, now)
    else:
        raise Exception(f"type: {data.type} is not a valid option")

def plot_pie(data: PlotData, time_stamp: str) -> Path:
    out_file = f"tmp/{time_stamp}-{data.type.name}.png"
    fig, ax = plt.subplots()
    ax.pie(
        [i.value for i in data.values],
        labels = [i.label for i in data.values],
    )
    ax.set(title = data.title)
    ax.set(xlabel = data.x_label)
    ax.set(ylabel = data.y_label)
    ax.plot()
    fig.savefig(out_file)
    return Path(out_file)

def plot_bar(data: PlotData, time_stamp: str) -> Path:
    out_file = f"tmp/{time_stamp}-{data.type.name}.png"
    fig, ax = plt.subplots()
    ax.bar(
        [i.label for i in data.values],
        [i.value for i in data.values],
    )
    ax.set(title = data.title)
    ax.set(xlabel = data.x_label)
    ax.set(ylabel = data.y_label)
    ax.plot()
    fig.savefig(out_file)
    return Path(out_file)

def plot_stacked(data: PlotData, time_stamp: str) -> Path:
    pass

