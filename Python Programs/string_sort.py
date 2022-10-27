
l=list(map(str,input("Enter the data").split()))
lst1 = sorted(l, key=lambda x:len(x))
print("Sorted list based on the length is : ", lst1)
lst2 = sorted(l, key = lambda x : len(list(set(x))))
print("Sorted list based on distinct character in string (ascending order)" ,lst2)
lst3 = sorted(l, key = lambda x : len(list(set(x))),reverse=True)
print("Sorted list based on distinct character in string (descending order)" ,lst3)
