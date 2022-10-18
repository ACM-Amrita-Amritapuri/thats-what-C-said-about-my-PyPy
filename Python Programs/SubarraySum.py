n=int(input())
def s(arr,start,end):
    res=0
    for j in arr:
        res+=ar[j]
    print(res)
    return res
for _ in range(n):
    k=int(input())
    ar=list(map(int,input().split()))
    m=0
    max_so_far = -1000
    max_ending_here = 0
    for i in range(0, k):
        max_ending_here = max_ending_here + ar[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    print(max_so_far)
