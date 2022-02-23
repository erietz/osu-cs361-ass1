import unittest
from src.plot import plot_data, plot_pie, plot_bar, plot_stacked, get_time_stamp
from pathlib import Path
from src.types import PlotData, PlotValues, PlotType

def generate_test_data(type: int):
    test_data = PlotData(
        title = "Backyard Grill out Revenue",
        x_label = "Taco Meats",
        y_label = "Sales / Trillion $",
        type = type,
        values = [
            PlotValues(label="Carne Asada", value=502),
            PlotValues(label="Chorizo", value=324),
            PlotValues(label="Barbacoa", value=122),
            PlotValues(label="Lengua", value=103),
            PlotValues(label="Birria", value=888),
            ]
        )
    return test_data


class Foo(unittest.TestCase):
    def test_plot_bar_with_valid_data_successfully(self):
        now = get_time_stamp()
        test_data = generate_test_data(PlotType.bar.value)
        image_path = plot_bar(test_data, now)
        self.assertTrue(image_path.exists())

    def test_plot_pie_with_valid_data_successfully(self):
        now = get_time_stamp()
        test_data = generate_test_data(PlotType.pie.value)
        image_path = plot_pie(test_data, now)
        self.assertTrue(image_path.exists())
