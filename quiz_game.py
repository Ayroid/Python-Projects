print("Welcome to my computer quiz!")
play=input("Do you want to play the Game? Yes 😄 or No 😶 ? > ")
if play.lower() == "no":
    print("Have a Good Day! 😉")
    quit()
score=0
print("Okay! Let's play 😄")

answer=input("What does CPU stands for? ")
if answer.lower()=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does GPU stands for? ")
if answer.lower()=="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does RAM stands for? ")
if answer.lower()=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does ROM stands for? ")
if answer.lower()=="read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("Final Score:",score)
