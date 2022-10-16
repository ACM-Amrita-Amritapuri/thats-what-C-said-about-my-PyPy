import random

mn, mx = 1,6
choice = 'Y'
while choice == 'YES' or choice == 'Y':
    n = int(input("How many dices do you want to roll? Please insert a number:  "))
    print('Dice is being rolled...')
    print('The value/values is/are-  ')
    for i in range(n):
        print(random.randint(mn,mx))
    x = input("Roll again? [Y]es, [N]o:  ")
    choice = x.upper()

print('Thank you!!')