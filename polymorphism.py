#creating a complex number
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def shown(self):
        print(f"{self.real}i+{self.imaginary}j")

s1=Complex(1,2)
s1.shown()

s2=Complex(3,4)
s2.shown()

print()
# we can find sum by
class Complex1:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def show(self):
        print(f"{self.real}i+{self.imaginary}j")

    def add(self,num2):
        newreal=self.real+num2.real
        newimaginary=self.imaginary+num2.imaginary
        return Complex1(newreal, newimaginary)

s1=Complex1(1,2)
s1.show()

s2=Complex1(3,4)
s2.show()

n3=s1.add(s2)
n3.show()

#or we can use doneder method
print()
class Complex2:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def show(self):
        print(f"{self.real}i+{self.imaginary}j")
    def __add__(self, other):
        newreal=self.real+other.real
        newimaginary=self.imaginary+other.imaginary
        return Complex2(newreal, newimaginary)
s1=Complex2(1,2)
s2=Complex2(3,4)
s3=s1+s2
s3.show()