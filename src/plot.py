from src.types.plot_data import PlotData
import matplotlib.pyplot as plt


def plot_data(plot_list: list[PlotData]):
    probable_value = 0.0
    absolute_error = 0.0
    relative_error = 0.0

    for data_calc in plot_list:
        probable_value += data_calc.probable_value
        absolute_error += data_calc.absolute_error
        relative_error += data_calc.relative_error

    probable_value = probable_value / plot_data.__sizeof__()
    absolute_error = absolute_error / plot_data.__sizeof__()
    relative_error = relative_error / plot_data.__sizeof__()

    data = [probable_value, absolute_error, relative_error]
    colun_names = ["Valor Provavel", "Erro Absoluto", "Erro Relativo"]
    positions = range(len(data))

    plt.bar(positions, height=data)
    plt.xticks(positions, colun_names)

    plt.show()
