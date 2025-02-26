'''
1 for snake
-1 for water
0 for gun
'''

import random

computer = random.choice([1,-1,0])
youstr = (input("Enter your choice: "))
youDict = {"s": 1, "w": -1, "g": 0}
reversedDict = {1:"snake", -1:"water", 0:"gun"}
you = youDict[youstr]

print(f"you choose {reversedDict[you]} \ncomputer chooese: {reversedDict[computer]} ")

if(computer==you):
    print("its's a draw...")
else:
    if(computer==-1 and you == 1):
        print("you win... And Computer looe")
    elif(computer==-1 and you == 0):
        print("yOU LOOSE AND Computer win....")
   
    elif(computer==1 and you==-1):
        print("YOU LOOSE AND Computer win...")
    elif(computer==0 and you ==-1 ):
        print("You win...")
    elif(computer==0 and you==1):
        print("you loose...")    
    else:
        print('Something went to wrong....')   
                         