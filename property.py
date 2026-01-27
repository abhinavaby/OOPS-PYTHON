class Student:
    def __init__(self,phy,che,math):
        self.phy=phy
        self.che=che
        self.math=math
        self.avg=str((self.phy+self.che+self.math)/3)+"%"
s1=Student(90,90,90)
print(s1.avg)
s1.phy=89
print(s1.avg)# if we chang the marks but the avg won't change

#so to change it we can do:
class Student2:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math
        # Initialize avg
        self.avg = str((self.phy + self.che + self.math) / 3) + "%"

    def per(self):
        # Update the existing self.avg attribute
        self.avg = str((self.phy + self.che + self.math) / 3) + "%"
        # Return the value so it can be printed
        return self.avg

s2 = Student2(90, 90, 90)
print(s2.avg)      # Output: 90.0%

s2.phy = 56        # Changing phy value
print(s2.phy)      # Output: 56

# Calling per() now updates s2.avg AND returns the new value
print(s2.per())    # Output: 78.66666666666667%

#this will work ,to make it more simpler we can use the @property


class Student3:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math


    @property
    def percentage(self):
       return str((self.phy + self.che + self.math) / 3)+"%"

s3 = Student3(90, 90, 90)
      # Output: 90.0%

s3.phy = 56        # Changing phy value
print(s3.percentage)