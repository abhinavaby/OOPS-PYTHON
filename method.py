#methods are functions belong to an object
class student:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def welcome(self):
        print(f"welcome student, {self.name}, age: {self.age}")
    def display(self):
        return self.mark





s1=student("abhinav",18,100)

s1.welcome()
mark=s1.display()
print(f"mark={mark}")