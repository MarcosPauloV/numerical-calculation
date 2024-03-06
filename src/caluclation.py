from math import sqrt


class Calculation:
    @staticmethod
    def absolute_error(vp: float, v1: int) -> float:
        return vp - v1

    @staticmethod
    def probable_value(n: int, v1: float) -> float:
        vp = 0.0
        for i in range(1, n + 1):
            vp += v1 / i
        return vp

    @staticmethod
    def relative_error(ea: float, vp: float) -> float:
        return (sqrt(ea**2) / vp) * 100
