class Plot:
    def __init__(
        self, probable_value: float, absolute_error: float, relative_error: float
    ):
        self.probable_value = probable_value
        self.absolute_error = absolute_error
        self.relative_error = relative_error
