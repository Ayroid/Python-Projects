import random

print("Welcome to the Guessing Game!🎉")
play=input("Do you want to play? Yes 😄  or No 😶 ? ")

if play.lower()!="yes":
    print("Have a Good Day! 😄")
    quit()
print("Let's Start 🥳")
rand=input("Enter the max limit > ")

if rand.isdigit():
    rand=int(rand)

    if rand<=0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()

randum=random.randint(0,rand)
ctr=1
while True:
    if ctr==1:
        guess=(input("Take your Guess > "))
    else:
        guess=(input("Take Another Guess > "))
    
    if guess.isdigit():
        guess=int(guess)
    else:
        print("Enter a number next time!  😑")

    if(guess==randum):
        print(f"Yeah! You Got it! in {ctr} attempts 🥳  🎉  🎊")
        break
    elif(guess>randum):
        print("You're a bit higher!")
    else:
        print("You're a bit lower!")
    ctr+=1