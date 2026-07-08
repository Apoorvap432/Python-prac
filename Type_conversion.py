#implicit type conversion - automatically done by python interepretor 
a = 10
b = 1.5
c = a+b
print(c)
d = True
e = a + d 
print(e)
f = False
g = a + f
print(g)


#explicit type conversion - it needs to be done by the programmer. Requires manual interventionn

h = "10"
i = 3 + int(h)
print(i)
j = float(h)
print(j)