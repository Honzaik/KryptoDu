
#uloha 2
M = 256
#eukliduv algoritmus pro pocitani inverzu
def eGCD(a, b):
    posledniZb = a if a>b else b
    zb = b if a>b else a
    posledniU = 1
    posledniV = 0
    u = 0
    v = 1
    while zb != 0:
        q = posledniZb // zb
        temp = zb
        zb = posledniZb - q * temp
        posledniZb = temp
        temp = u
        u = posledniU - q*temp
        posledniU = temp
        temp = v
        v = posledniV - q * temp
        posledniV = temp

    return (posledniU, posledniV) if a>b else (posledniV, posledniU)

#šifrovaci funkce
def enKAS(plaintext, a, b, c):
    ciphertext = list()
    for x in plaintext:
        y = (x+a) % M
        ciphertext.append((y*c + b) % M)
    return ciphertext
#dešifrovaci funkce
def deKAS(ciphertext, a, b, c):
    plaintext = list()
    for x in ciphertext:
        y = (x-b) % M
        cInv = eGCD(c, M)[0]
        y = (y*cInv) % M
        plaintext.append((y-a) % M)
    return plaintext
#test
p = [1,2,3,5,0,8] #"plaintext"
a = 5
b = 240
c = 253

e = enKAS(p,a,b,c)
print(e) #ciphertext
print(deKAS(e,a,b,c)) #dešifrovaný ciphertext, mělo by se rovnat p

'''
##úloha 3
##########################
import random
s = ""
for i in range(1000): # text dlouhý 1000 znaků
    s = s + chr(65+random.randint(0,25))

def getFrekvence(s):
    frekvence = list()
    for i in range(26):
        frekvence.append(0)

    for c in s:
        frekvence[ord(c) - ord('A')] += 1
    return frekvence


def getIC(s):
    frekvence = getFrekvence(s)
    sum = 0
    for i in range(26):
        sum += frekvence[i]*(frekvence[i]-1)
    return round(sum/(len(s)*(len(s)-1)), 3)

print(getIC(s))
'''