# method for accessing file
f = open("text.txt")   #yaha r mtlv read krna
data = f.read
print(data)
f.close

# iska alternate method using with
with open("file.txt") as f:
    print(f.read())


'''
jaha pe "r" likha hai vha kya kya aa skta hai? 

f = open("text.txt", "r")  

r -> read
w -> write
a -> appending     -> kisi chij k end mein kuch jodna 
+ -> updating
'rb' -> read in binary mode
'rt' -> read in text form

'''