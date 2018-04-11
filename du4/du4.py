def deg(x):
    deg = -1;
    if(x != 0):
        for i in range(100):
            bit = ((0b1 << i) & x) >> i
            if(bit == 0b1):
                deg = i
    return deg

def polyNas(x,y):
    f = x
    g = y
    m = deg(g)
    res = 0b0
    for i in range(m+1):
        bit = ((0b1 << i) & g) >> i
        if(bit == 0b1):
            res ^= f << i

    return res

#return x div y
def polyDiv(x,y):
    f = x
    g = y
    if(deg(y) > deg(x)):
        f = y
        g = x
    n = deg(f)
    m = deg(g)
    r = f
    q = 0b0
    for i in range(n-m,-1,-1):
        q_i = (((0b1) << (i+m)) & r) >> i+m #bit u x^(i+m) v r
        q |= q_i << i
        if(q_i == 0b1):
            r ^= g << i
    return (q,r)

#eukliduv algoritmus pro pocitani inverzu
def eGCD(a, b):
    old_r = a
    r = b
    if(deg(b) > deg(a)):
        old_r = b
        r = a
    old_u = 1
    old_v = 0
    u = 0
    v = 1
    while r != 0:
        (q, zb) = polyDiv(old_r, r)
        temp = r
        r = zb
        old_r = temp
        temp = u
        u = old_u ^ polyNas(q,temp)
        old_u = temp
        temp = v
        v = old_v ^ polyNas(q,temp)
        old_v = temp
    if (deg(b) > deg(a)):
        return (old_r, old_v, old_u)
    else:
        return (old_r, old_u, old_v)

POLY = 0b110000111

def invert(element):
    (gcd, u, v) = eGCD(element, POLY)
    if(gcd != 1):
        print("CHYBA")
        return -1
    else:
        return u

print("result of inversion: " + str(invert(200)))