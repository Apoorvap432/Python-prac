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