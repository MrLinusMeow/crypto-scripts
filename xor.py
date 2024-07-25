def xor(input, key):
    i = len(input)
    t = bytearray(input, 'ascii')
    j = len(key)
    k = bytearray(key, 'ascii')
    while i != 0:
        i -= 1
        j -= 1
        t[i] ^= k[j]
        if j == 0:
            j = len(key)
    return t.decode('ascii')

print(xor(">/$-)2p<1:2/$)50.p43p-$)523s", "]"))
