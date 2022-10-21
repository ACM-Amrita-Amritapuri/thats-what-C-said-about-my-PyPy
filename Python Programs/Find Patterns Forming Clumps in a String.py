sequence = input("Enter the genomic sequence")
k = int(input("Enter the length k of each kmer"))
L = int(input("Enter the length of clump L"))
t = int(input("Enter the minimum times t"))
DNA = str(sequence.upper())
counts = {}
for i in range(0, len(DNA) - k + 1):
    kmer = DNA[i:i + k]
    if kmer in counts:
        counts[kmer] += 1
    else:
        counts[kmer] = 1
frequent = {}
for k in counts:
    if counts[k] >= t:
        frequent[k] = counts[k]
answer = frequent.keys()
output = ' '.join(answer)
print(output)