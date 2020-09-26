from math import sqrt, floor
import time
from libnum import invmod
from sympy import factorint


def main():
        print(crackRsaPrivateKey(7, 33))

def crackRsaPrivateKey(e, n):
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
        d = invmod(e, phi)
        return d

main()
