from time import sleep

class TrafficLight:
    __color  = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        i = 0
        while i < 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(1)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(2)
            i += 1

a = TrafficLight()
print(a.running())


























