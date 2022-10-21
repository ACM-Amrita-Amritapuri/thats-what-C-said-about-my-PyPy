def Rev(DNA):
    return DNA[::-1]
def Comp(DNA):
    d = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A','\n':''}
    Complement_DNA = ''
    for i in DNA:
        Complement_DNA = Complement_DNA+d[i]
    return Complement_DNA
def Reverse_Complement(DNA):
    Com = Comp(DNA)
    RComp = Rev(Com)
    return RComp
f = open("rosalind_revc.txt","r")
rev = Reverse_Complement(f.read())
print(rev)