class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Arjun",18)
del s1.name
print(s1.age)
print(s1.name)
