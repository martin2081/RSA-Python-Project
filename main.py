# Martin Luna Project 3 RSA

import math


# determine if its prime
def mrt(x):
    if x == 2 or x == 3:
        return True
    # prime numbers must be greater 1 and not even
    elif x <= 1 or x % 2 == 0:
        return False
    elif x > 3:
        for i in range(2, int(x/2)+1):
            if (x % i) == 0:
                return False
        else:
            return True


# euclidean algorithm function
def ea(a, b):
    # math function
    return math.gcd(a, b)


# extended euclidean algorithm
# gcd(r0, r1) = s0 *r0 + t0 *r1
def eea(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b != 0:
        q = int(a / b) # quotient
        r = a % b # remainder
        a, b = b, r
        s1, s0 = s0 - q * s1, s1
        t1, t0 = t0 - q * t1, t1
    print(s0, t0)
    return s0, t0


def modular_inverse(e, n):
    # e^-1, mod n
    i = pow(e, -1, n)
    return i


# square and multiply algorithm
# same code use for the homeworks
def powmod_sm(base, exp, n):
    exp_b = bin(exp)
    value = base

    for i in range(3, len(exp_b)):
        value = (value ** 2) % n
        if exp_b[i:i+1] == '1':
            value = (value * base) % n
    return value


def rsa_key_gen(p, q):
    if p != q:
        mrt(p)
        mrt(q)
    n = p * q
    phi = (p - 1) * (q - 1)
    # choose i when the gcd is 1
    # has to start from 2
    for i in range(2, 200):
        if ea(i, phi) == 1:
            e = i
            break
    d = modular_inverse(e, phi)
    return n, e, d


def main():
    # two prime numbrs p & q
    mrt(23)
    mrt(29)
    p = 23
    q = 29
    print("Prime number p = 23")
    print("Prime number q = 29")

    # calculate n and phi
    n, e, d = rsa_key_gen(p, q)
    # public key
    print(f"Kpub = ({n}, {e})")
    # private key
    print(f"Kpr = {d}")
    x = 124
    print(f"Plaintext: {x}")
    y = powmod_sm(x, e, n)
    print(f"Ciphertext: {y}")
    dec = powmod_sm(y, d, n)
    print(f"Original: {dec}")


main()

