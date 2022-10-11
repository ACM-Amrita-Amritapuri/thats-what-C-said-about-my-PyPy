def Multiply(A,B):
    if len(str(A)) == 1 or len(str(B)) == 1:
        return A*B
    else:
        l = max(len(str(A)),len(str(B)))
        n = l // 2
        al = A // 10**(n)
        ar = A % 10**(n)
        bl = B // 10**(n)
        br = B % 10**(n)
        result = ((10**(2*n))*Multiply(al,bl))+((10**n)*(Multiply((al+ar), (bl+br))-Multiply(al,bl)-Multiply(ar,br)))+Multiply(ar,br)
        return result
A=int(input())
B=int(input())
print(Multiply(A,B))