n = int(input())
ribbon = [0]*3
for i in range(3):
    string = input()
    A = [0]*256
    for j in range(len(string)):
        A[ord(string[j])] += 1

    score = 0
    for j in range(len(A)):
        score = score if score > A[j] else A[j]

    if score == len(string) and n==1:
        score = len(string) - 1
    else:
        score += n
        score = score if score < len(string) else len(string)
    ribbon[i] = score

if ribbon[0] > ribbon[1] and ribbon[0] > ribbon[2]:
    print('Kuro')
elif ribbon[1] > ribbon[0] and ribbon[1] > ribbon[2]:
    print('Shiro')
elif ribbon[2] > ribbon[0] and ribbon[2] > ribbon[1]:
    print('Katie')
else:
    print('Draw')

