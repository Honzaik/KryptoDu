
def binToBitArray(num):
    result = []
    numList = list(str(num))
    for i in range(len(numList)):
        result.append(int(numList[i]))
    return result[::-1]

def bitArrayToInt(bitArray):
    result = 0
    for i in range(len(bitArray)-1,-1,-1):
        result = bitArray[i] + 2*result
    return (result)

def permutation(input): #16 bit input
    input = binToBitArray(f'{input:0>16b}')
    output = []
    for i in range(16):
        output.append(0)
    for i in range(16):
        newI = int((i/4) + (i%4) * 4)
        output[newI] = input[i]
    return bitArrayToInt(output)

def sbox(input): #4bit input
    inputNum = int(input)
    TABLE = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]
    subbedNum = TABLE[inputNum]
    return subbedNum

def key_addition(input, key): #xor 2 čísel
    return input ^ key

def round(input, key):
    output = permutation(input)
    s1Result = sbox(((output & 0x000f) >> 0))
    s2Result = sbox(((output & 0x00f0) >> 4))
    s3Result = sbox(((output & 0x0f00) >> 8))
    s4Result = sbox(((output & 0xf000) >> 12))
    output = s1Result + (s2Result << 4) + (s3Result << 8) + (s4Result << 12)
    output = key_addition(output, key)
    return output

vstup = 0xf00d
print(round(vstup, 0xf2f2))
