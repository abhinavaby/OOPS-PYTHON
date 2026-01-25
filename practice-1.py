class student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def avg(self):
        return (self.mark1+self.mark2+self.mark3)/3
while True:
    name=input("enter your name:")
    if name=="quit":
        break
    mark1=input("enter your mark1:")
    mark2=input("enter your mark2:")
    mark3=input("enter your mark3:")
    mark1=float(mark1)
    mark2=float(mark2)
    mark3=float(mark3)
    s1=student(name,mark1,mark2,mark3)
    avg=s1.avg()
    print(f"avg={avg}")
