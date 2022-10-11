def Count(txt,pattern):
    count = 0
    txt = txt+" "
    for i in range(len(txt)-len(pattern)):
        if (txt[i:i+len(pattern)] == pattern):
            count = count+1
    return count
file = open("rosalind_ba1a.txt",'r')
data=file.readlines()
a =data[0].strip()
b =data[1].strip()
print(Count(a,b))