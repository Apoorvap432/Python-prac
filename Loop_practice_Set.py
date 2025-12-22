#generate a table using for loop
print("----1. Table of 6----")
for i in range(6, 61, 6):
    print(i)

print("----Table of 6 using function----")
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")



print("----2. Greet all the persons name stored in list l whose names start with A----")
l = ["Appu", "Arnav", "Sejal", "Suraj"]
for name in l:
    if(name.startswith("A")):
        print(f"Hello {name}")



# problem 1 using while loop
print("----3. Table using while loop----")
tab = int(input("Enter a number: "))
i = 1
while(i<11):
    print(f"{tab} * {i} = {tab*i}")
    i += 1



#no. prime or not
print("----4. Whether number is prime or not----")
num = int(input("Enter the number: "))
for i in range (2, n):
    if(n%i == 0):
        print("Number is not prime")
    break
else:
    print("Number is prime")



# sum of natural numbers
print("----5. sum of first n natural numbers using while loop----")
n = int(input("Enter the number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i += 1
print(sum)



#factorial
print("----6. Calculate factorial using for loop----")
num = int(input("Enter the no. whose factorial u want: "))
#5! = 5*4*3*2*1
fact = 1
for i in range(1, num+1):
    fact *= i
print(f"The factorial of {num} is: ", fact)



''' Star pattern
  *
 ***
*****
for n = 3
'''
print("----7. Program to print the star pattern for n = 3----")
n = int(input("Enter the value of n: "))
for i in range (1, n+1):
    print(" " * (n-i), end = "")
    print("*" * (2*i-1), end = "")
    print()



# multiplication table of n using for loop in reversed order
print("----10. multiplication table of n using for loop in reversed order----")
n = int(input("Enter the number: "))
for i in range (1, 11):
    print(f"{n}*{11-i}={n*(11-i)}")
