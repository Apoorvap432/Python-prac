#inheritance
class Employee():
    Company = "Walmart"
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")

class Programmer(Employee):
    Company = "HCL"
    def showLanguage(self):
        print(f"The name of the employee is {self.name} and the fav language of him/her is {self.language}")

a = Employee()
b = Programmer()

print(a.Company, b.Company)


#---------------multiple inheritance - 2 parent 1 child--------------- 

class Dog():
    Name = "Sheru"
    Breed = "German Shephard"
    def dogShow(self):
        print(f"The name of dog is {self.Name} and the breed is {self.Breed}")

class Cat():
    name = "Billu"
    def catShow(self):
        print(f"The name of the cat is {self.name}")

class AnimalResult(Dog, Cat):
    Result = "Dangerous"
    def ResultShow(self):
        print(f"If we take the dog of breed {self.Breed} and name {self.Name} with the cat of name {self.name}, the result will be {self.Result}")

c = Dog()
d = Cat()
e = AnimalResult()

c.dogShow()
d.catShow()
e.ResultShow()



#---------------multilevel inheritance - parent -> child -> child--------------- 

class A():
    a = 1

class B(A):
    b = 2

class C(B):
    c = 3

f = A()
print(f.a)

f = B()
print(f.a, f.b)

f = C()
print(f.a, f.b, f.c)