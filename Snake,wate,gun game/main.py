'''
1 for snake
-1 for water
0 for gun
'''
import random

computer=random.choice([0,-1,1])
youstr=input("Enter your choice:")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]

reverseDict={1:"Snake",-1:"Water",0:"gun"}
print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer==you):
    print("It's a draw!")

else:
    if(computer==-1 and you==1):
        print("You win!")
    elif(computer==-1 and you==0):
        print("You lose!")

    elif(computer==1 and you==-1):
        print("You lose!")
    elif(computer==1 and you==0):
        print("You win!")

    elif(computer==0 and you==1):
        print("You lose!")
    elif(computer==0 and you==-1):
        print("You win!")

    else:
        print("Something went wrong!")