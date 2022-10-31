def myfun(number1 ,number2):
    product = number1*number2
    if product<=1000:
        return product
    else:
        return number1 + number2
result = myfun(20,30)
print(result)
