import random 

Logo = """

   ____                       _____ _            _   _                 _                 _ 
  / ___|_   _  ___  ___ ___  |_   _| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __  | |
 | |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| | |
 | |_| | |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |    |_|
  \____|\__,_|\___||___/___/   |_| |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|    (_)
                                                                                           

"""

print(Logo)

print('Welcome to game "Guess The Number!"')

random_number = random.randint(1, 100)

level = input('Choose a level "easy" or "hard": ').lower()
if level == "easy":
    chances = 9
    print("You have 10 chances to guess the number.")
else:
    chances = 4
    print("You have 5 chances.")

# print(random_number)

for chance in range(chances, -1 , -1):
    guess = int(input("Guess a number between 1 to 100: "))

    if guess == random_number:
        print(f"You Win! The correct number is {random_number}!")
        break

    if guess > random_number:
        print("Too high!")
        print(f"You have {chance} chances left.")

    if guess < random_number:
        print("Too low!")
        print(f"You have {chance} chances left.")

    if chance == 0:
        print("You lose! You lost all chances!")
        print(f"The correct number is {random_number} ")
