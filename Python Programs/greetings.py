#greeting in different languages
name = input("Name: ")
print("Which language do you prefer:")
n = input()

if n == "English":
    print("Hello, ",name)
elif n == "Spanish":
    print("Hola, ",name)
elif n == "French":
    print("Bonjour, ",name)
elif n == "Italian":
    print("Salve, ",name)
else:
    print("Wrong entry :(")