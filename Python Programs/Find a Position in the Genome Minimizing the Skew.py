def skew(dna):
    c,g,min = 0,0,0
    list = []
    index = 0
    for i in dna:
        index += 1
        if i == 'C':
            c += 1
        if i == 'G':
            g += 1
            skew = g-c
        if skew < min:
            list = [index]
            min = skew
        if skew == min and index not in list:
            list.append(index)
    for i in list:
        print(i,end=' ')
dna=input('Enter the DNA sequence: ')
skew(dna)