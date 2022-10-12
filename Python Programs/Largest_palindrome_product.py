import sys
from itertools import combinations
import operator
import bisect

t = int(input().strip())
def pali(k):
    return True if k == int(str(k)[::-1]) else False
p = sorted(set(filter(pali,map(lambda x: operator.mul(*x),combinations(tuple(range(100,1000)),2)))))
for a0 in range(t):
    n = int(input().strip())
    print(p[0:(bisect.bisect_left(p,n))][-1])
