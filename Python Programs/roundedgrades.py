grades=[73,67,38,33]
rounded_grades=[]
for x in grades:
    if x>37:
        for i in range(3):
            if (x+i)%5==0:
                print(x+i)
                rounded_grades.append(x+i)
        if(x+3)%5==0:
            rounded_grades.append(x)
    else:
        rounded_grades.append(x)
print(rounded_grades)