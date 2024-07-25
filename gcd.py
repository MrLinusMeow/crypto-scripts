def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

tu = 0
tv = 0
def ext_gcd(a, b):
    if a == 0:
        return 0, 1
    x1, y1 = ext_gcd(b%a, a)
    x = y1 - (b//a) * x1
    y = x1

    return x,y

def test():
    u = 0
    v = 0
    p = 26513
    q = 32321
    a = 10
    b = 15

    print(min(ext_gcd(p, q)))
    print(gcd(a, b))
    print(gcd(b, a))

test()
