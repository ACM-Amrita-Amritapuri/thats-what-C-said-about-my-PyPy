import os

def countingValleys(steps, path):
    v = 0
    t = 0
    for i in path:
        if i == "U":
            t += 1
            if t == 0:
                v += 1
        else:
            t -= 1
    return v
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

