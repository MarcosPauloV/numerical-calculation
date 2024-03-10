class Heartbeat:
    def __init__(self, n: int, v1: int):
        self.n = n
        self.v1 = v1

    def __str__(self) -> str:
        return f"{self.n}, {self.v1}"

    def __repr__(self) -> str:
        return f"{self.n} {self.v1}"
