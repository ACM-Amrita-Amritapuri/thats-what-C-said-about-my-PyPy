#Program to grade student marks
mar=int(input("Enter the marks"))
if mar>=90:
 print("Your grade is A1")
elif mar>=80 and mar<90:
 print("Your grade is A2") 
elif mar>=70 and mar<80:
 print("Your grade is B1") 
elif mar>=60 and mar<70:
 print("Your grade is B2") 
elif mar>=50 and mar<60:
 print("Your grade is C1") 
elif mar>=40 and mar<50:
 print("Your grade is C2") 
elif mar>=30 and mar<40:
 print("Your grade is D") 
else:
 print("Your grade is E (failed)")
