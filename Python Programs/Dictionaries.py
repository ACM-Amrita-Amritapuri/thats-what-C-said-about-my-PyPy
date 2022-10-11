d={}
s="String"
for x in s.split(" "):
    if x not in d:
        d[x]=1
    else:
        d[x]+=1
for x in d:
    print(x,d[x])