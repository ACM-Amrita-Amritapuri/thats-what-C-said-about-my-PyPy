import sys
n=10**6
prime=[]
l={}
def sieve():
    prime=[True for i in range(n+1)]
    prime[0]=prime[1]=False
    p=2
    while p*p<=n:
        if prime[p]==True:
            for j in range(p*p,n+1,p):
                if prime[j]:
                    prime[j]=False
        p+=1
    temp=0
    for i in range(2,n+1):
        if prime[i]:
            temp+=i
        l[i]=temp
    
t = int(input().strip())
sieve()
for a0 in range(t):
    n = int(input().strip())
    print(l[n])
