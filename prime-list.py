def prime(max):
    r = []
    p = 2
    while p != max:
        d = 1
        p += 1
        while d != p:
            d += 1
            if (p % d) == 0:
                break
            if d == p - 1:
                r.append(p)
    return r

print(prime(pow(2,16)))
