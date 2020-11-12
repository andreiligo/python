class Stationery:
    title = 'Рисование'

    def draw(self):
        return print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        return print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        return print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        return print('Запуск отрисовки маркером')



a = Pen()
b = Pencil()
c = Handle()

print(a.draw())
print(b.draw())
print(c.draw())