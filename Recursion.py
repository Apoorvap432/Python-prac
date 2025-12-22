#Recursion is a function which calls itself 

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number whose factorial you want: "))
print(f"Factorial of the number is: {factorial(n)}")