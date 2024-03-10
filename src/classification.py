def classification(value: int):
    if value < 70:
        return "Abaixo"
    elif value > 70:
        return "Acima"
    else:
        return "Dentro"
