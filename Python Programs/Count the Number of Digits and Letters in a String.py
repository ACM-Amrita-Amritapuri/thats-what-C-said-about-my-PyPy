#Program to count the Number of Digits and Letters in a String
string = input("Enter a string : ")

def countLetterAndDigits(string):
    lcount = dcount = 0
    for c in string:
        if c.isdigit():
            dcount+=1
        elif c.isalpha():
            lcount+=1
    return lcount, dcount

letters, digits = countLetterAndDigits(string)

print("No of letters/alphabets : ", letters)
print("No of digits : ", digits)