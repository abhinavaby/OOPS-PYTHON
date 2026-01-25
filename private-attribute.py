class Account:
    def __init__(self, balance, acc_no,password):
        self.balance = balance
        self.acc_no = acc_no
        self.__password = password #private
    def resetpass(self):
        self.__password = "1ase"
s1=Account(balance=10000, acc_no='123', password='asdas')
print(s1.balance)
print(s1.acc_no)
#print(s1.__password) wont give the value to the object


class Person:
    __name="Abhinav"
    def __hello(self):
        print("hello")
    def print(self):
        self.__hello()
s1=Person()
#print(s1.__name)
#print(s1.__hello)
s1.print()