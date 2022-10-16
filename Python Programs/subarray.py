for i in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    
    while p:
        y=""
        for k in range(len(p)):
            y+=(str(p[k])+" ")
            print(y)
            
        p.pop(0)