from random import randint

#class programmer with employee details

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry", 1200000, 251307)
print(p.name, p.salary, p.pin, p.company)

r = Programmer("Henry", 1250000, 251001)
print(r.name, r.salary, r.pin, r.company)



#class calculator capable of finding square, cube, square root of a number. 
class calculator:

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The square is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The square is {self.n**1/2}")

    #static method
    @staticmethod
    def greet():
        print("Hello user")

a = calculator(4)
a.square()
a.cube()
a.squareroot()
a.greet()


# Add class train which has methods to book tickets, get status(no. of seats), and get fair info of train running under indian railways

class train:

    def __init__(self, trainNum):
        self.trainNo = trainNum

    def book(self, frm, to):
        print(f"Train is booked from {frm} to {to}")

    def status(self):
        print(f"Train number {self.trainNo} is running 10 mins late.")

    def fair(self, frm, to):
        print(f"The fair for train {self.trainNo} from {frm} to {to} is {randint(225, 2000)}")\
        
a = train(35245)
a.book("Muzaffarnagar", "Delhi")
a.status()
a.fair("Muzaffarnagar", "Delhi")