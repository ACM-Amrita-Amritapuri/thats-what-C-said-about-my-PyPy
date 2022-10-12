import sys
import random

while True:
    val=input("Enter the top range : ")

    try:
        top_rang = int(val)
    except ValueError:
        print("Enter a valid number please :) !")
        continue
    

    randval = random.randrange(0,top_rang)

    ans_guessed = False

    remarks = ["Congratulation!!!!!","Awesome!!!","Nice!!","Good"]

    for i in range(4):

        guess = int(input("Take a guess : "))

        if guess==randval:
            print(f"{remarks[i]}, you have correctly guessed the value in {i+1} tries")
            ans_guessed = True
            break
        else:
            print("Wrong guess mate :(")
    
    if(ans_guessed==False): print("Better Luck next time")


    while True:
        choice = input("Would you like to continue with the game ? (y/n)")

        if choice.lower()=="n" : sys.exit()

        elif choice.lower()=="y": 
            print() 
            break

        else:
            print("Please Enter a valid answer :) !")
            print()