burger=input()
need=[0 for _ in range(3)]
need[0]=burger.count('B')
need[1]=burger.count('S')
need[2]=burger.count('C')
have=[float(item) for item in input().split()]
price=[float(item) for item in input().split()]
budget=float(input())
minBurger = 0
maxBurger = 100000000000000
while minBurger <= maxBurger:
    total_cost = 0
    middle = (minBurger + maxBurger) // 2
    for i in range(0, 3):
        tmp = have[i] - need[i] * middle
        if tmp < 0:
            total_cost += abs(tmp) * price[i]
    if total_cost <= budget:
        ans = middle
        minBurger = middle + 1
    else:
        maxBurger = middle - 1
print(ans)