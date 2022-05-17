class Cell:
    def __init__(self, x, y, value=0):
        self.pos = x, y
        self.value = value

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)