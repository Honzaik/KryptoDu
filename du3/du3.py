def permutation(input): #16 bit input
    res = 0b0
    for i in range(16):
        bit = (0b1 << i) & input
        if (bit != 0b0):
            posun = int((i / 4) + (i % 4) * 4) - i
            if (posun >= 0):
                bit = bit << posun
            else:
                bit = bit >> (posun * -1)
            res |= bit
    return res

def sbox(input): #4bit input
    inputNum = int(input)
    TABLE = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]
    subbedNum = TABLE[inputNum]
    return subbedNum

def key_addition(input, key): #xor 2 čísel
    return input ^ key

def round(input, key):
    output = key_addition(input, key)
    s1Result = sbox(((output & 0x000f) >> 0))
    s2Result = sbox(((output & 0x00f0) >> 4))
    s3Result = sbox(((output & 0x0f00) >> 8))
    s4Result = sbox(((output & 0xf000) >> 12))
    output = s1Result + (s2Result << 4) + (s3Result << 8) + (s4Result << 12)
    output = permutation(output)
    return output

vstup = 0xf00d
key = 0x1111
print(hex(round(vstup, key)))
