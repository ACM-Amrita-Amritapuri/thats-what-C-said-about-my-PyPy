alphabet = {'a','b','c','d','e','f','g','h',' ','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
sentence=set(input('enter a sentence'))
if alphabet ==sentence:
    print ("pangram")
else:
    print("not a pangram")
    
alphabet = {'a','b','c','d','e','f','g','h',' ','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
sentence=set(input('enter a sentence'))
a=['pangram' if alphabet==sentence else 'not a pangram']
print(a)
