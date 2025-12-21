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


'''
to use pass:

Agar hm kisi loop pe kaam kr rhe h aur use bich m chd k hm koi or loop pe kaam krne lgte h to vo 
incomplete loop error throw krega. Us error se bachne k liye hm us incomplete loop k baad pass 
likh dega to vo function us loop k liye na ruk k use pass kr dega next loop ko
'''