s = input("Enter DNA Sequence: ")
s =s.upper()
code=['A','T','G','C']
dna=list(s)
f = True
for i in range(len(dna)):
    fl = dna[i] in code
    f = f and fl
    if(f==False):
        break
if (f==True):
    mrna = s.replace('T','U')
    print("DNA: ",s," is transcribed to mRNA of sequence: ",mrna)
else:
    print("Sequence is wrong")