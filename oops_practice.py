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



#