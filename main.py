#SNAKE WATER AND GUN GAME 

import random
'''
1 for snake
-1 for water
0 for gun
'''

Bot = random.choice([-1,0,1])
youstr = input("enter your choice: ")
youdict = {"s":1, "w":-1, "g":0}
reversedict = {1:"snake", -1:"water", 0:"gun"}

you = youdict[youstr]

print(f"Your choice {reversedict[you]} \n Bot choice {reversedict[Bot]}")

if(Bot==-1 and you==-1):
    print("Draw")

else:

    if(Bot==-1 and you==1):
        print("yay!!!!! You Win")
    
    elif(Bot==-1 and you==0):
        print("Bot win")

    elif(Bot==1 and you==-1):
        print("Bot Win")

    elif(Bot==1 and you==0):
        print("You Win")

    elif(Bot==-0 and you==-1):
        print("Bot Win")

    else:
        print("choose your option!!!!") 


# shortend version of same

'''
if((Bot - you)==-1 or (Bot - you)==2):
    print("you lose")

else:
    print("You win")
    
'''