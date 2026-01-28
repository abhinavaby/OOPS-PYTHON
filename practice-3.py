class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.perimeter = 2 * self.radius * 3.14
    def area(self):
        return 3.14 * (self.radius ** 2)
s1=Circle(3)
print(f'AREA: {s1.area()}')
print(f"perimeter: {s1.perimeter}")