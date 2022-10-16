import random
import sys

print('Welcome to the game')
print('Rock, Paper, Scissors')
print('Let\'s begin')
choices = ['R', 'P', 'S']
while(1):
    print("Choose your move: ")
    x = input("[R]ock, [P]aper, [S]cissors:  ")
    userChoice = x.upper()
    if userChoice not in choices:
        print('Please choose a letter from R,P and S')
        sys.exit()
    else:
        computerChoice = random.choice(choices)
        print('I chose: '+computerChoice)
        if computerChoice == userChoice:
            print("It's a Tie!")
        elif computerChoice == 'R' and userChoice=='S':
                print("Scissors beats rock, I win! ")
                continue

        elif computerChoice == 'S' and userChoice.upper() == 'P':
            print("Scissors beats paper! I win! ")
            continue

        elif computerChoice == 'P' and userChoice.upper() == 'R':
            print("Paper beat rock, I win!")
            continue

        else:
            print("Congratulations!!! You win!")
            sys.exit()