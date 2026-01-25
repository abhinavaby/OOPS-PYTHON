class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    Varc="welcome to class C"
d=C()
print(d.varA)
print(d.varB)
print(d.Varc)
