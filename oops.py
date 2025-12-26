#  class -- contains the info to create a valid object

class Employee:
    name = "Apoorva"
    age = 22
    salary = 0

    #use of self
    def getInfo(self):
        print(f"The age of {self.name} is {self.age} and salary is {self.salary}.")

    #static method
    #yaha pe greet function ko obj ki ya self ki jrurt ni h islye hm ise static method bol denge
    @staticmethod
    def greet():
        print("Good morning")


    #dundun method - ye automatically call hoga jb bhi koi naya obj bnega 
    def __init__(self):
        print("obj created")

apoorva = Employee()
print(apoorva.name, apoorva.age)
apoorva.getInfo()
apoorva.greet()