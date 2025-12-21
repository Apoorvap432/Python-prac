'''for loop'''

for i in range(1, 12):
    print (i)

'''another method'''
for j in range(1, 70, 5):
    print(j)


print("----tuple list-----")
'''tuple'''
t = (1, 24, 75)
for i in t:
    print (i)

print("----list-----")
li = [34, 43, 12, 21]
for i in li:
    print(i)


print("----name characters----")
name = 'Apoorva'
for i in name:
    print(i)


print("--- with else----")
i = 1

for i in range(1, 4):
    print (i)
else:
    print("no more nos left")