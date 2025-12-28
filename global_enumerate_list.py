a = 45

def fun():
    a = 3
    print(a)

fun()
print(a)


#enumerate
l = [3, 513, 53, 535]

for index, item in enumerate(l):
    print(f"The item at index {index} is {item}")


#list comprehensions
myList = [1, 4, 6, 34, 9]

squaredList = [i*i for i in myList]

print(squaredList)