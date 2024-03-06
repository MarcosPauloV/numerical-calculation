from src.get_data import get_data
from src.types.plot_data import Plot
from src.plot import plot_data
from src.caluclation import Calculation


plot_list: list[Plot] = []

for heartbeat in get_data():
    probable_value = Calculation.probable_value(heartbeat.n, heartbeat.v1)
    absolute_error = Calculation.absolute_error(probable_value, heartbeat.v1)
    relative_error = Calculation.relative_error(absolute_error, probable_value)

    plot_list.append(Plot(probable_value, absolute_error, relative_error))

plot_data(plot_list)
