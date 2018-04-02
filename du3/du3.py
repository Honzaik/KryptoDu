
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

#vstup = 0xf00d
#print(round(vstup, 0x0002))

pc1 = [56, 48, 40, 32, 24, 16,  8,
		  0, 57, 49, 41, 33, 25, 17,
		  9,  1, 58, 50, 42, 34, 26,
		 18, 10,  2, 59, 51, 43, 35,
		 62, 54, 46, 38, 30, 22, 14,
		  6, 61, 53, 45, 37, 29, 21,
		 13,  5, 60, 52, 44, 36, 28,
		 20, 12,  4, 27, 19, 11,  3]
left_rotations = [
		1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
	]

pc2 = [
		13, 16, 10, 23,  0,  4,
		 2, 27, 14,  5, 20,  9,
		22, 18, 11,  3, 25,  7,
		15,  6, 26, 19, 12,  1,
		40, 51, 30, 36, 46, 54,
		29, 39, 50, 44, 32, 47,
		43, 48, 38, 55, 33, 52,
		45, 41, 49, 35, 28, 31
	]
def permutate(table, block):
	return list(map(lambda x: block[x], table))

key1 = [1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0]
#print(key1)
permutedKey = permutate(pc1, key1)
print(permutedKey)
L = permutedKey[:28]
R = permutedKey[28:]
print(L)
print(R)
print("###################################xx")
#0x1fe01fe01fe01fe k11
L = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] #K11
R = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] #K11

#K1 pár druhý
#0xfe01fe01fe01fe01 k12
#L = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] #K12
#R = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] #K12
###################
#0x1FE01FE00EF10EF1 k21
#L = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] #K21
#R = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] #K21

#K2 pár druhý
#0xE01FE01FF10EF10E k22
#L = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] #K22
#R = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] #K22

#0x1FFE1FFE0EFE0EFE
#L = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] #K31
#R = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] #K31
#0xFE1FFE1FFE0EFE0E
#L = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] #K32
#R = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] #K32

#print(L)
#print(R)
K = list()
i=0
while i < 16:
    j = 0
    # Perform circular left shifts
    while j < left_rotations[i]:
        L.append(L[0])
        del L[0]

        R.append(R[0])
        del R[0]

        j += 1

    # Create one of the 16 subkeys through pc2 permutation
    print("#####################")
    print(L)
    print(R)
    K.append(permutate(pc2, L+R))
    print(str(i+1) + ": " + str(K[i]))
    i += 1

#print(K)
'''
KRev = K[::-1]
for i in range(16):
    b = 1
    print(str(i+1) + ": " + str(KRev[i]))
'''
L = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] #K11
R = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] #K11
L = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] #K12
R = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] #K12
K11 = L+R
KInv = []
for i in range(64):
    KInv.append(0)

for i in range(len(pc1)):
    KInv[pc1[i]] = K11[i]
print(KInv)

#for i in range(8):
#    print(KInv[8*i:8*(i+1)])

K11Real = [0, 0, 0, 0, 0, 0, 0, 1,
           1, 1, 1, 1, 1, 1, 1, 0,
           0, 0, 0, 0, 0, 0, 0, 1,
           1, 1, 1, 1, 1, 1, 1, 0,
           0, 0, 0, 0, 0, 0, 0, 1,
           1, 1, 1, 1, 1, 1, 1, 0,
           0, 0, 0, 0, 0, 0, 0, 1,
           1, 1, 1, 1, 1, 1, 1, 0]
K12Real = [1, 1, 1, 1, 1, 1, 1, 0,
           0, 0, 0, 0, 0, 0, 0, 1,
           1, 1, 1, 1, 1, 1, 1, 0,
           0, 0, 0, 0, 0, 0, 0, 1,
           1, 1, 1, 1, 1, 1, 1, 0,
           0, 0, 0, 0, 0, 0, 0, 1,
           1, 1, 1, 1, 1, 1, 1, 0,
           0, 0, 0, 0, 0, 0, 0, 1]

print(K12Real)
s = ''
for i in range(64):
    s += str(K12Real[i])

#s = s[::-1]
print(s)
print(hex(int(s,2)))
#0x1fe01fe01fe01fe k11
#0xfe01fe01fe01fe01 k12