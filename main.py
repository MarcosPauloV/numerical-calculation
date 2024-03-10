from src.get_data import get_data
from src.plot import plot_data
from src.caluclation import Calculation


list_data = get_data()

for heartbeat in list_data:
    probable_value = Calculation.probable_value(heartbeat.n, heartbeat.v1)
    absolute_error = Calculation.absolute_error(probable_value, heartbeat.v1)
    relative_error = Calculation.relative_error(absolute_error, probable_value)

    print(f"Valor Provavel: {probable_value}")
    print(f"Erro Absoluto: {absolute_error}")
    print(f"Erro Relativo (%): {relative_error}")


plot_data(list_data)
