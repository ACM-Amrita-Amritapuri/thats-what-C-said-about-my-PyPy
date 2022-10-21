#Let’s use continue to write a program that asks for a name and password
while True :
    print('Enter your name!')
    name = input()
    if name != 'Saumy' :
        continue
    else :
        print('Welcome Saumy! Please enter your password. Hint(It is a kind of fish)')
        pwd = input()
        if pwd != 'swordfish' :
            continue
    print('Access granted !')
    break