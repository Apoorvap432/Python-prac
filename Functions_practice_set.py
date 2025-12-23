#function to find max of 3 nos
def max(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
x = int(input("Enter the first no.: "))
y = int(input("Enter the second no.: "))
z = int(input("Enter the third no.: "))        
print("The maximum number among the three is: ", max(x, y, z))



#use fucn to convert farhenhiet to celsius 
#formula: c/5 = (f-32)/9
def conversion(f):
    return ((f-32)/9)*5

f = int(input("Enter temperature in farhenhiet: "))
print(conversion(f))



#how to prevent python print() to print a new line at the end
print("a", end = "")
print("v")
#last mein ye end = "" likhne se is line aur iski agli line k bich koi space ni hoga na hi ye agli line mein honge



#function to find sum of n natural numbers
def sum(n):
    if(n==1):
        return 1
    else:
        return sum(n-1) + n

print(sum(7))



#fucn to print first n lines of the following patten
# ***
# ** 
# *

def pattern (n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)


#func which converts inches to cms
def inchConversion(inch):
    return inch*2.54

n = int(input("Enter inches to be converted into cms: "))
print(f"The corresponding value in cms is: {inchConversion(n)}")