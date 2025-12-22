def greet(name, ending):
    print("Hello bhai " + name + " " + ending)


greet("Appu", "Kya haal hai?")
greet("Apoorva ji", "kaise ho?")

def greet1(name):
    print("Hello " + name)
    return "puch lia haal chaal"

a = greet1("Appu")
print (a)



#default parameter
def animal(name, sound="don't know"):
    print("Name of animal is: " + name + " and sound is: " + sound)

#agar hm 2nd vala parameter denge to vo show hoga output mein ni to jo fucn mein diya h vhi use hoga
animal("Cat", "Meow")
animal("Camel")

