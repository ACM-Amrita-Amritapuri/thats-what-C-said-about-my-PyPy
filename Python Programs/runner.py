if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    s=set(arr)
    
    g=sorted(s)
    print(g[(len(s)-2)])
    