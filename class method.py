  #to change class attributes from object
class Person:
    name="anonymous"
    def changename(self,name):
        self.name=name

p1=Person()
p1.changename("Abhinav")
print(p1.name)
print(Person.name)

print()
print()



class Person2:
    name="anonymous"
    def changename(self,name):
        Person2.name=name

p1=Person2()
p1.changename("Abhinav")
print(p1.name)
print(Person2.name)


print()
print()
class Person3:
    name="anonymous"
    def changename(self,name):
        self.__class__.name=name

p1=Person3()
p1.changename("Abhinav")
print(p1.name)
print(Person3.name)

print()
print()

class Person4:
    name="anonymous"
    @classmethod
    def changename(cls,name):
        cls.name=name

p1=Person4()
p1.changename("Abhinav")
print(p1.name)
print(Person4.name)







