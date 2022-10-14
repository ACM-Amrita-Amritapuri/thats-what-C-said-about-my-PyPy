#Program to count vowels
sentence = input("Enter any string:")
sentence = sentence.lower()
vowel_count = 0
for i in sentence:
    if i == "a" or i == "e" or i == "i" or i == "o" or i =="u":
        vowel_count = vowel_count + 1
print("Total vowel count : ", vowel_count)

