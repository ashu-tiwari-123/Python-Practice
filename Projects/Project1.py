# snake water and gun game

import random

print("Enter s for Snake \nEnter w for Water \nEnter g for Gun")
print("--------------------------------------------------------")

computer = random.choice([-1,0,1])
youDict = {
    "s":1,
    "w":-1,
    "g":0,
}
youNum = input("Enter Your choice:")
you = youDict[youNum]
reverseDict = {
    1:"Snake",
    -1:"Water",
    0:"Gun"
}
print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")
if(computer == you):
    print("its a draw!")
else:
    if(computer == 1 and you == -1):
        print("you Lose!")
    elif(computer ==1 and you == 0):
        print("You won!") 
    elif(computer == -1 and you == 1):
        print("you won!")
    elif(computer ==-1 and you == 0):
        print("You Lose!") 
    elif(computer == 0 and you == 1):
        print("you Lose!")
    elif(computer == 0 and you == -1):
        print("You Won!") 
    else:
        print("Something went wrong! Try again")    

