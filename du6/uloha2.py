import math

def RC4Output(key, n):

    #init
    S = list()
    for i in range(256):
        S.append(i)

    j = 0
    for i in range(256):
       j = (j + S[i] + key[i % len(key)]) % 256
       temp = S[i]
       S[i] = S[j]
       S[j] = temp

    i = 0
    j = 0
    output = list()
    for k in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        output.append(S[(S[i] + S[j]) % 256])
    return output

target = (0xef, 0xf8, 0x5b, 0x0b, 0x95, 0x14, 0xff, 0x09, 0xcb, 0x0e)

key = 0

while key < 2**16:
    keyList = (key % 256, math.floor(key / 256))
    output = RC4Output(keyList, len(target))
    print(output)
    if len(set(output) & set(target)) == len(target):
        print(keyList)
        print(key)
        break
    key += 1

#13330 <=> 0x3412