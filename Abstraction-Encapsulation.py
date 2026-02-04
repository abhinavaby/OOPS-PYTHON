#Abstraction:hiding the important details of a class and only showing the essential features to the user
#Abstraction
import time
class car:
    def __init__(self):
        self.acc=False #Abstraction
        self.brk=False #Abstraction
        self.clutch=False #Abstraction
    def start(self):
        self.acc=True #Abstraction
        self.brk=True #Abstraction
        self.clutch=True #Abstraction
        print("starting"=" ")
        for i in range(6):
            print(".",end=" ")
            time.slee
        print("started")
s1=car()
s1.start()

#Abstracted data not found in output(for the user )


#Encapsulation:Wrapping data and functions into a single unit(object).
#Encapsulation
class student:
    def __init__(self,fullname,age):
        self.fullname=fullname
        self.age=age
        print(f"hello {fullname} you are {age} years old")
        print(self)


fullname=input("enter fullname")
age=int(input("enter age"))
s1=student(fullname,age)
print(s1)


s2=student("Arjun",18)
print(s2.fullname)
print(s2.age)




