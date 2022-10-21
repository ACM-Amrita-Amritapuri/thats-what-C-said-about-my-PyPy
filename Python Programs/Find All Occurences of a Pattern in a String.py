def startindex(txt,pattern):
    txt = txt+" "
    l = []
    for i in range(len(txt)-len(pattern)):
        if (txt[i:i+len(pattern)] == pattern):
            l.append(i)
    x = ' '.join([str(n) for n in l])
    return x
file = open("rosalind_ba1d.txt",'r')
f = file.readlines()
k = f[0].strip()
m = f[1].strip()
print(startindex(m,k))