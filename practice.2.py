class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no

a1=Account(1000000,1234)
print(a1.balance)
print(a1.acc_no)
print("1:credit,2:debit")
out=int(input())
if out==1:
    n=int(input("enter the amount to be credited: "))
    a1.balance+=n
    print(f"current balance is {a1.balance}")
elif out==2:

    n=int(input("enter the amount to be debit: "))
    a1.balance-=n
    print(f"current balance is {a1.balance}")
else:
    print("error")