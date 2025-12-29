from functools import reduce


#Lambda function - fucn using lambda keyword
#lambda arguments - expressions
square = lambda x: x*x
print(square(5))
sum = lambda a,b,c: a+b+c
print(sum(3, 6, 2) )



#join - hm jo bhi likhege join k sth to vo usi k sth list k elements ko join kr dega 
nameList = ["Appu", "Apoorva", "Appuuzz"]
final = "::".join(nameList)
print(final)



#map, filter and reduce 
#map
l = [1, 2, 3, 4, 5]
square = lambda x: x*x
sqList = map(square, l)
print(list(sqList))

#filter
def even(n):
    if(n%2 == 0):
        return True
    return False
onlyEven = filter(even, l)
print(list(onlyEven))

#reduce
'''
1 + 2   3   4   5
|   |   |   |   |
  3   + 3   |   |
  |     |   |   |
     6    + 4   |
     |      |   |
        10    + 5
        |       |
            15
'''
def sum(a, b):
    return a+b
print(reduce(sum, l))