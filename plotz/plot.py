from datetime import datetime
from matplotlib import pyplot as plt
from pathlib import Path
import seaborn as sns

from .types import PlotData, PlotType

sns.set_theme(style="darkgrid", palette="Set3")

def get_time_stamp() -> str:
    return datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

def remove_tmp_image(path: Path) -> None:
    path.unlink(missing_ok=True)

def plot_data(data: PlotData) -> Path:
    now = get_time_stamp()
    if data.type == PlotType.pie.name:
        return plot_pie(data, now)
    elif data.type == PlotType.bar.name:
        return plot_bar(data, now)
    elif data.type == PlotType.stacked.name:
        return plot_stacked(data, now)
    else:
        raise Exception(f"type: {data.type} is not a valid option")

def plot_pie(data: PlotData, time_stamp: str) -> Path:
    out_file = f"tmp/{time_stamp}-{data.type.name}.png"
    values = [i.value for i in data.values]
    labels = [i.label for i in data.values]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels, autopct='%.1f%%')
    ax.set(title = data.title)
    fig.tight_layout()
    ax.plot()
    fig.savefig(out_file, transparent=True)
    return Path(out_file)

def plot_bar(data: PlotData, time_stamp: str) -> Path:
    out_file = f"tmp/{time_stamp}-{data.type.name}.png"
    labels = [i.label for i in data.values]
    values = [i.value for i in data.values]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set(title = data.title)
    ax.set(xlabel = data.x_label)
    ax.set(ylabel = data.y_label)
    fig.tight_layout()
    ax.plot()
    fig.savefig(out_file, transparent=True)
    return Path(out_file)

def plot_stacked(data: PlotData, time_stamp: str) -> Path:
    pass

