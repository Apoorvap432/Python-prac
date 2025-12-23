import random
'''
0 for snake
1 for water
2 for gun 

Snake drinks water → Snake wins
Water douses gun → Water wins
Gun kills snake → Gun wins
'''

computer = random.choice([0, 1, 2])
youStr = input("Enter your choice: ")
yourDict = {"s":0, "w": 1, "g":2}
you = yourDict[youStr]

if(computer == you):
    print("Match draw!")
else: 
    if(computer == 0 and you == 1):
        print("You lose!")
    elif(computer == 0 and you == 2):
        print("You won!")

    elif(computer == 1 and you == 0):
        print("You won!")
    elif(computer == 1 and you == 2):
        print("You lose!")

    elif(computer == 2 and you == 0):
        print("You lose!")
    elif(computer == 2 and you == 1):
        print("You won!")

    else:
        print("Something went wrong!")