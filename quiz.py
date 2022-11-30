print("Welcome to my Quiz!!")

playing = input("Begin quiz? ")

if playing.lower()!= "yes":
    quit()
 
print("Great! Let's begin:)")
score=0

answer=input("What does CPU stand for? ")
if answer.lower()== "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer=input("What does a.k.a stand for? ")
if answer.lower()== "also known as":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer=input("What is 1+1? ")
if answer.lower()== "2":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer=input("Can you spell bee? ")
if answer.lower()== "bee":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer=input("How do you spell red? ")
if answer.lower()== "red":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got " + str(score/5 *100) + "%!")
