from src.types.plot_data import Plot
import matplotlib.pyplot as plt


def plot_data(plot_list: list[Plot]):
    probable_value = 0
    absolute_error = 0
    relative_error = 0
    acceptable_count = 0
    below_count = 0
    above_count = 0

    for data_calc in plot_list:
        probable_value += data_calc.probable_value
        absolute_error += data_calc.absolute_error
        relative_error += data_calc.relative_error

        if data_calc.relative_error <= 5:
            acceptable_count += 1
        elif data_calc.relative_error > 5:
            above_count += 1
        else:
            below_count += 1

    probable_value = probable_value / len(plot_list)
    absolute_error = absolute_error / len(plot_list)
    relative_error = relative_error / len(plot_list)

    data = [probable_value, absolute_error, relative_error]
    column_names = ["Valor Provável", "Erro Absoluto", "Erro Relativo"]
    positions = range(len(data))

    plt.bar(positions, height=data)
    plt.xticks(positions, column_names)
    plt.xlabel("Métricas")
    plt.ylabel("Valores")
    plt.title("Métricas de Dados")

    plt.figure()

    categories = ["Dentro do Padrão", "Abaixo do Padrão", "Acima do Padrão"]
    counts = [acceptable_count, below_count, above_count]
    plt.bar(categories, counts, color=["green", "blue", "red"])
    plt.xlabel("Categoria")
    plt.ylabel("Quantidade")
    plt.title("Análise da Taxa de Pulsação")

    plt.show()
