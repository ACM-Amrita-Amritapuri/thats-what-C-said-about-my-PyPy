s=input("Enter DNA sequence: ")
code=["A","T","G","C"]
s=s.upper()
dna=list(s)
f=True
for i in range(len(dna)):
    fl=dna[i] in code
    f=f and fl
    if(f==False):
        break
if(f==True):
        a=dna.count("A")
        c=dna.count("C")    
        g=dna.count("G")
        t=dna.count("T")
        print("A: ",a,"\nC: ",c,"\nG: ",g,"\nT: ",t)
else:
        print("Sequence is wrong")