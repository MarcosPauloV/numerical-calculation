from src.get_data import get_data
from src.types.plot_data import PlotData
from src.plot import plot_data
from src.caluclation import Calculation


data = get_data()
probable_value = 0.0
absolute_error = 0.0
relative_error = 0.0
plot_list: list[PlotData] = []

for heartbeat in data:
    probable_value = Calculation.probable_value(heartbeat.n, heartbeat.v1)
    absolute_error = Calculation.absolute_error(probable_value, heartbeat.v1)
    relative_error = Calculation.relative_error(absolute_error, probable_value)

    plot_list.append(PlotData(probable_value, absolute_error, relative_error))

plot_data(plot_list)
