class Clothes: # создаем класс Clothes
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_1(self):
        return self.width / 6.5 + 0.5

    def get_square_2(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Clothes): # класс с наследованием от Clothes
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_1 = round(self.width / 6.5 + 0.5)


    def __str__(self):
        return f'Площадь пальто {self.square_1}' # вывод сообщения


class Jacket(Clothes):
    def __init__(self, width,height):
        super().__init__(width, height)
        self.square_2 = round(self.height / 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_2}'

coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_1())
print(jacket.get_square_2())
