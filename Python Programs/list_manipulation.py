lst1=["study", 'Eat','sleep',"eat","Walk","Study","eat"]
#Adding ing to each element
for i in range(0,len(lst1)):
  lst1[i]+="ing"
print(lst1)   

#find 'sleep' in the list and replace it with dance.
for i in range(0,len(lst1)):
    if(lst1[i]=="sleep"):
       lst1[i]="dance"
print(lst1)        

#create a list with unique elements from lst1.
unique=[]
for i in lst1 :
  if i not in unique:
     unique.append(i)
  else:
     pass
print(unique)  

#remove all occurrences of “eat” from lst1.
for j in range (0,len(lst1)-1):
     if(lst1[j]=="eat"):
        lst1.remove("eat")
print(lst1)       

# sort the list in alphabetical order.
lst1.sort()
print(lst1)

# Add elements that occur more than twice in lst1 to a new list.
lst1=["study", 'Eat','sleep',"eat","Walk","Study","eat"]
unique=[]
c=0
j=0
for i in lst1 :
    c=0
    for j in lst1:
       if(i==j):
         c+=1
    if(c>=3):
        unique.append(i)
print(set(unique))  
