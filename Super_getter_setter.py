#super class

class A():
    def __init__(self):
        print("A is running!")
    a = 1

class B(A):
    def __init__(self):
        print("B is running!")
    b = 2

class C(B):
    def __init__(self):
        super().__init__()      #iska use krne pe jo iski super class hogi vo bhi run kregi. 
        print("C is running!")
    c = 3


f = C()
print(f.a, f.b, f.c)


#class attribue
#maan lo hmare pas hai ye

class Num():
    a = 23
    def show(self):
        print(f"The number is {self.a}")

e = Num()
e.a = 45
print(e.a)

# agar hm ye upar vla run krege to ye 45 hi print krega. to agar hm chahte hai ki ye 45 nahi balki class attribute (23) print kre to hm ye niche vla run krege
class Num():
    b = 23
    @classmethod
    def show(cls):
        print(f"The number is {cls.b}")

e = Num()
e.b = 45
print(e.show())