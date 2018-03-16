import random
import math

s = ""
for i in range(1000): # text dlouhý 1000 znaků
    s = s + chr(65+random.randint(0,25))

def nthCharString(s, n):
    newString = ""
    for i in range(len(s)):
        if((i % n) == 0):
            newString += s[i]
    return newString

def getFrekvence(s, abeceda):
    frekvence = {}
    for c in abeceda:
        frekvence[c] = 0
    for c in s:
        frekvence[c] += 1
    return frekvence

#delka klice
def getIC(s, abeceda, n):
    strings = list()
    ICs = list()
    for i in range(n):
        urizlaS = s[i:]
        newS = nthCharString(urizlaS, n)
        strings.append(newS)
        frekvence = getFrekvence(newS, abeceda)
        sum = 0
        for c in abeceda:
            sum += frekvence[c]*(frekvence[c]-1)
        ICs.append(round(sum/(len(newS)*(len(newS)-1)), 3))

    return ICs, strings

ABECEDA = "!',.;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = "NHKHY;''DKGAC!ZW'MH!.TWSZXTCGAOM,RDSE.HPYU';!HY;X'JB'XXNGNNBLQXNJ!HYUEXE.BER;GNIYTG.'GH.TG.'JNGFHDSDNYF.Q;BYYE.UA;FNTTDSE.GYC'GQHI!RMNHKHY;.JGYY;UVGNNWBO.GKESF.Q;BYYE.BZOUZBOBHNZ?ERX';E!EA;JH!Q!UBZK!TTTS';EHE.;JB?!L;HXOGHXXWGNZHE.;JBOY!VB'QNYUR;GNIYTHVV?NUFTYTN!!DRN'HLYE.UA;FNTTDSDNYLDUVHPHY;DSKIX!O,MOIQO;BZSLTTBMGNNB,URMO'HE.;JBOEYU'FNZBU,BZHZXTUVNH!UBAXGE?M;BCGNHISUUR,O!O;YAMEMD,XG!RB'KCVMOHLQXNJCG!OVYK!RM"
delkaKlice = 7
ics, strings = getIC(s, ABECEDA, delkaKlice)
print(ics)
print(strings)
frekvence = list()
for i in range(delkaKlice):
    frekvence.append(getFrekvence(strings[i], ABECEDA))


relCetnostPlaintext = [0.015, 0.01, 0.021, 0.022, 0.0, 0.005, 0.075, 0.016, 0.022, 0.034, 0.106, 0.014, 0.027, 0.06, 0.061, 0.001, 0.012, 0.044, 0.022, 0.06, 0.076, 0.013, 0.002, 0.054, 0.053, 0.079, 0.037, 0.009, 0.023, 0.001, 0.025, 0.0]
cetnostPlaintext = {}
sum = 0;
for i in range(len(relCetnostPlaintext)):
    pocet = round(relCetnostPlaintext[i]*len(s))
    sum += pocet
    cetnostPlaintext[ABECEDA[i]] = pocet

cetnosti = {'U': 0.037, 'B': 0.016, 'D': 0.034, 'M': 0.022, 'T': 0.079, 'K': 0.012, 'I': 0.061, 'R': 0.054, 'O': 0.076, 'L': 0.044, 'V': 0.009, 'H': 0.06, '.': 0.022, "'": 0.01, '?': 0.005, 'Y': 0.025, '!': 0.015, 'C': 0.022, 'N': 0.06, 'E': 0.106, 'S': 0.053, ',': 0.021, 'F': 0.014, 'Q': 0.002, 'P': 0.013, 'J': 0.001, 'A': 0.075, 'G': 0.027, 'Z': 0.0, ';': 0.0, 'W': 0.023, 'X': 0.001}
print(sorted(cetnosti.items(), key=lambda x:x[1]))



def desifruj(s, klic):
    desifrovanyText = ""
    for i in range(len(s)):
        index = (ABECEDA.find(s[i])^ABECEDA.find(klic[i%len(klic)]))
        #print(str(i) + ": " + s[i] + " xor " + klic[i % len(klic)] + " = " + ABECEDA[index])
        desifrovanyText += ABECEDA[index]
    return desifrovanyText

klic = "PYTONIK"
#print(s)
desif = desifruj(s, klic)

print(desif)

print(desifruj("JVQ!WCRBNWKNNRKMSGLMO.YE.?MYVCPXH?ANQNEARXLCXT", "GO.UQV.;SZ?NOOS?PMNCTXCJVICF;BE'NETNXCN?JKHUMD"))
#print(getIC(desif, ABECEDA, 1))
print(cetnostPlaintext)
print(getFrekvence(desif, ABECEDA))
xored = ".JPUENO.F.P!B.CRHY,UHYQ?SFUPZJZWYJZ!FVT.SHWMJK"
#c2 = "GO.UQV.;SZ?NOOS?PMNCTXCJVICF;BE'NETNXCN?JKHUMD"
print(desifruj(xored, "XXXXXXXXXHATEDJABBERWOCKYKOAN"))

#print(desifruj("J;TIFR", "KLIC"))


