class Road:
    def __init__(self, length, width, mass):
        self._length = length
        self._width = width
        self._mass = mass

    def mass_f(self):
        return self._mass * self._length * self._width


a = Road(25, 100, 200)
print(a.mass_f())