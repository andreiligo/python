class Car:
    speed = 80
    color = 'Black'
    name = 'Volvo'
    is_police = False


    def go_method(self):
        return print('Car starting')


    def stop_method(self):
        return print('Car just have stopped')

    def turn_method(self, direction):
        self.direction = direction
        if direction == 'left':
            return print('Car is going to turn left')
        else:
            return print('Car is going to turn right')

    def show_speed(self):
        return print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print('Your speed is too high')


class SportCar(Car):
    def go_method(self):
        return print('GO GO GO')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print('Your speed is too high')

class PoliceCar(Car):
    def go_method(self):
        return print('Going to find some bad guys!')

print(Car.speed)
print(Car.name)
a = TownCar()
b = SportCar()
c = WorkCar()
a.turn_method('left')
b.stop_method()
c.show_speed()