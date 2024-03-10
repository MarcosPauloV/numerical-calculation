from src.types.heartbeat import Heartbeat
from src.classification import classification
import matplotlib.pyplot as plt


def plot_data(plot_list: list[Heartbeat]):
    classificated = [classification(value.v1) for value in plot_list]

    inside = classificated.count("Dentro")
    below = classificated.count("Abaixo")
    above = classificated.count("Acima")

    categories = ["Dentro", "Abaixo", "Acima"]
    values = [inside, below, above]

    plt.bar(categories, values, color=["green", "yellow", "red"])  # type:ignore
    plt.title("Distribuição da Taxa de Pulsação")  # type:ignore
    plt.xlabel("Classificação")  # type:ignore
    plt.ylabel("Número de Funcionários")  # type:ignore
    plt.show()  # type:ignore
