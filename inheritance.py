#one class derives the properties and method of oter class
class Car:
    color = "red"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class Toyota(Car):
    def __init__(self,brand):
        self.name=brand

car1=Toyota("Toyota")
car1.start()
car1.stop()
print(car1.color)
car2=Toyota("innova")
car2.start()
car2.stop()


class Fortuner(Toyota):
    def __init__(self,type):
        self.name=type
car3=Fortuner("disel")
car3.start()
car3.stop()
print(car3.color)
print(car3.name)















