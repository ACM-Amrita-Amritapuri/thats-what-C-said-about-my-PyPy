def Count(txt,pattern):
    count = 0
    txt = txt+" "
    for i in range(len(txt)-len(pattern)):
        if (txt[i:i+len(pattern)] == pattern):
            count = count+1
    return count
f = open("rosalind_ba1b.txt",'r')
file=f.readlines()
dna = file[0].strip()
dna = dna+" "
k = int(file[1].strip())
countm = 0
ptm = []
for j in range(len(dna)-k):
    pt = dna[j:j+k]
    count = Count(dna,pt)
    if(count>countm):
        ptm =[]
        countm = count
        ptt = pt
    elif(count == countm and pt not in ptm):
        ptm.append(pt)
print(" ".join(ptm))