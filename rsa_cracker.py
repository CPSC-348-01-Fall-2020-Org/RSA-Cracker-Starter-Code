from sympy.ntheory import factorint


def main():
    print(crackRsaPrivateKey(7, 33))

def crackRsaPrivateKey(e, n):
    """Given an RSA public key, return the private exponent."""
    factorsOfN = factorint(n)

    # since n is the product of two primes, we know its only factors are those two primes
    # if this is not the case, n is invalid (i.e., not the product of two primes)
    factorsAreValid = len(factorsOfN) == 2 and all(multiplicity == 1 for multiplicity in factorsOfN.values())
    if (not factorsAreValid):
        raise Exception(f"{n} is not a valid n value.")

    factorsList = list(factorsOfN)
    p = factorsList[0]
    q = factorsList[1]

    phi = (p - 1) * (q - 1)
    d = inverse_mod(e, phi)
    return d


def inverse_mod(a, m):
    """Return the inverse mod of a with respect to m."""
    g, x, y = extended_greatest_common_denominator(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def extended_greatest_common_denominator(a, b):
    """Return (g, x, y) such that a*x + b*y = g = greatest_common_denominator(a, b)."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_greatest_common_denominator(b % a, a)
        return (g, x - (b // a) * y, y)


main()
