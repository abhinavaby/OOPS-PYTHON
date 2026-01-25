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

