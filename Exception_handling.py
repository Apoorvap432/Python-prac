a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(b==0):
    raise ZeroDivisionError("This number can't be zero.")
else:
    print(f"The division is {a/b}")


#try with else
# ye else mein tbhi jaega jb try successful hoga

try:
    c = int(input("Enter any number: "))
    print(c)

except Exception as e:
    print(e)

else: 
    print("Try run successfully that's why I am inside else")



#try with finally
# ye finally mein jaega hi chahe try successful ho ya exception aae

try:
    d = int(input("Enter any number: "))
    print(d)

except Exception as e:
    print(e)

finally: 
    print("ye try run ho ya exception aae. finally tumhe finally k pas aana hi aana hai. ")