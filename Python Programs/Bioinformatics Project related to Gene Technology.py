import itertools
from operator import index
from tokenize import String

def findfreqwordswithmismatchbysort(text,k,d):

    freq_patterns = []

    neighbourhoods = []

    index = []

    count = []

    for i in range(len(text)-k):

        neighbourhoods.extend(d_neighbourhood(text[i:i+k],d))

    for i in range(len(neighbourhoods)-1):

        pattern = neighbourhoods[i]

        index.append(patt_to_num(pattern))

        count.append(1)

    temp = []


    for i in index:

        if(i!=None):

            temp.append(int(i))

    index=temp

    index.sort()

    for i in range(len(index)-1):

        if index[i] == index[i+1]:

            count[i+1]=count[i]+1

    maxcount = max(count)

    for i in range(len(neighbourhoods)-1):

        if(count[i]==maxcount):
            
            pattern = num_to_patt(index[i],k)

            freq_patterns.append(pattern)

    #print(index)
    return freq_patterns


def d_neighbourhood(text,d):

    neighbours = []

    lst = generate_unique_pattern(text)

    for i in lst:

        if(hamming_distance(i,text)<=d):

            neighbours.append(i)

    return neighbours


def hamming_distance(patt1 , patt2):

    hd = 0

    if(len(patt1)!=len(patt2)):

        print("Error!! length should be same for finding hamming distance")

        return
    else:
        for i in range(len(patt1)):

            if(patt1[i]!=patt2[i]):

                hd += 1

    return hd



def generate_unique_pattern(pattern):

    lst = list(itertools.product("ACGT",repeat=len(pattern)))

    for i in range(len(lst)):

        str = ""

        for j in lst[i]:

            str+=j

        lst[i]=str

    return lst

def patt_to_num(patt):

    if patt=="":

        return 0

    symbol = LastSymbol(patt)

    prefixpatt = prefix(patt)



    return 4*patt_to_num(prefixpatt) + Symbol_to_num(symbol)

def num_to_patt(index,k):

    if k ==1:

        return num_to_symbol(index)

    prefixind = index//4

    r= index % 4

    symbol = num_to_symbol(r)

    prefixpat = num_to_patt(prefixind,k-1)
    #print("=========================================>", prefixpat + symbol)

    return prefixpat+symbol

def Symbol_to_num(patt):

    symbol_map = {"A":0,"C":1,"G":2,"T":3}

    temp = 0

    for i in patt:

        temp = symbol_map.get(i)

    return temp

def num_to_symbol(patt):
    symbol_map = {0:"A",1:"C",2:"G",3:"T"}

    # temp = ""

    # for i in patt:

    #     temp+=symbol_map.get(i)

    if symbol_map.get(patt):
        return symbol_map.get(patt)
    else:
        return ""


def LastSymbol(patt):
    try:
        return patt[-1]
    except Exception:
        pass

def prefix(patt):

    return patt[0:-1]




genome = input("Enter genome : ")

k = int(input("Enter k value : "))

d = int(input("Enter d value : "))

output = findfreqwordswithmismatchbysort(genome,k,d)

print(*output)