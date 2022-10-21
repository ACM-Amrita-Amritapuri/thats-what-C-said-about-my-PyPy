def HammingDistance(dna1,dna2):
    hamming_distance=0
    if len(dna1)!=len(dna2):
        print('Given sesquence is not of same length')
    else:
        for i in range (0,len(dna1)):
            if dna1[i] != dna2[i]:
                hamming_distance+=1
    return hamming_distance
dna1=input('Enter the first dna sequence - ')
dna2=input('Enter the second dna sequence - ')
print('The Hamming distance is - ',HammingDistance(dna1,dna2))