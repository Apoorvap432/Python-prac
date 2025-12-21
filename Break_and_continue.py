for i in range(1, 6):
    if( i == 4):
        break   #yaha pe exit kr dega loop
    print(i)

for j in range(1, 6):
    if( j == 4):
        continue    # ye vala iteration skip kr dega
    print(j)


l = ["Appu", "is", "a", "good", "girl"]
for i in l:
    if i == "good":
        break
    print (i)

for j in l:
    if j == "good":
        continue
    print(j)