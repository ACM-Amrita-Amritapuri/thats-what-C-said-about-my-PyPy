# Python program to show how the for loop works  
  
# Creating a sequence which is a tuple of numbers  
numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]  
  
# variable to store the square of the number  
square = 0  
  
# Creating an empty list  
squares = []  
  
# Creating a for loop  
for value in numbers:  
    square = value ** 2  
    squares.append(square)  
print("The list of squares is", squares)  
