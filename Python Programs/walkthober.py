n=int(input())


for _ in range(n):
     l1=list(map(int,input().split()))
     k=[]
     for i in range(l1[0]):
          l2=list(map(int,input().split()))
          k.append(l2)
    
     s=0
     for j in range(l1[1]):
          mx=[]
          for i in range(l1[0]):
               mx.append(k[i][j])
        
          if max(mx)>= mx[l1[2]-1]:
               s=s+(max(mx)-mx[l1[2]-1])
     print("Case #"+str((_+1))+": "+str(s))
