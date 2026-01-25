class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("starting...")
    @staticmethod
    def stop():
        print("stopping...")

class Toyota(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()
car1=Toyota("Innova","suv")
print(car1.name)
print(car1.type)
