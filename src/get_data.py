from src.types.heartbeat import Heartbeat


def get_data() -> list[Heartbeat]:
    with open("src/database/pulso.txt", "r") as file:
        content = file.readlines()

    n_pulso: list[Heartbeat] = []

    for line in content:
        n, v1 = line.split("\t")
        n, v1 = int(n.strip()), int(v1.strip())
        n_pulso.append(Heartbeat(n, v1))

    return n_pulso
