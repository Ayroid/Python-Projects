from operator import indexOf
import random

print("Rock Paper Scissors")

play=input("Do you want to play? Yes 😄  or No 😶  ? ")

if play.lower() != "yes":
    print("Let's play some other day! 😄")
    quit()

print("\nLet's Start 🥳\n")

comp=0
user=0
user_choice=""
comp_choice=""

opt=["Rock","Paper","Scissors"]
opt2=["R","P","S"]
print("Enter:\nR: Rock\nP: Paper\nS: Scissors\nQ: Quit")

while True:
    user_choice=input("\nChoose: ").capitalize()

    if user_choice in opt2:
        user_choice=opt[opt2.index(user_choice)]

    if user_choice == "Q":
        print("\nThanks for Playing! 😉")
        if comp>0 or user>0:
            print(f"\nFinal Score:\nComputer: {comp}  You: {user}\n")
            if(user>comp):
                print("\n🥳 🥳  YOU WON! 🥳 🥳\n")
            elif(user<comp):
                print("YOU LOST! 😅\n")
            else:
                print("😉 😉  DRAW 😉 😉\n")
        break

    if user_choice not in opt:
        print("Please choose from the options!")
        continue

    val=random.randint(0,2)
    comp_choice=opt[val]
    print("\nYou Chose:",user_choice)
    print("Computer picked:",comp_choice+"\n")

    if user_choice=="Paper" and comp_choice=="Rock":
        user+=1
        print("Yay! You won 🥳\n")
    
    elif user_choice=="Rock" and comp_choice=="Scissors":
        user+=1
        print("Yay! You won 🥳\n")

    elif user_choice=="Scissors" and comp_choice=="Paper":
        user+=1
        print("Yay! You won 🥳\n")

    elif user_choice==comp_choice:
        #user+=1
        #comp+=1
        print("Draw! 😅")

    else:
        comp+=1
        print("You Lost! 🙁\nLet's play again!\n")