import sys

# Message Codes
CODE_ARG     = 0
CODE_FAIL    = 1

# Message Texts
MSG = [
    'Number of Arguments does not match the Expected.\nUsage: python pollardRhoAttack.py <N> <B>',
    'FAILURE. Unable to factorize the large prime.'
]

if len(sys.argv) != 3:
    print(MSG[CODE_ARG])
    sys.exit(1)

def gcd(a, b):
    """ Returns gcd(a, b) """
    """ Complexity: O( log^3(N) ) """
    if a > b:
        return gcd(b, a)

    if a == 0:
        return b

    return gcd(b % a, a)

def moduloPower(a, i, N):
    """ Returns a**i (mod N) """
    """ Complexity: O( log(B) * log^2(N) ) """
    val = 1
    while i > 0:
        if i % 2:
            val *= a
            val %= N
        a *= a
        a %= N
        i //= 2  # Use integer division for Python 3
    return val

def pollardRhoAttack(a, N, B):
    """ Implementation of Pollard's Rho - 1 Attack """
    """ Worst Case Complexity: O( ( B * log(B) + log(N) ) * log^2(N) ) """

    # computing a**(B!) (mod N)
    for i in range(2, B + 1):  # Use range instead of xrange for Python 3
        # computing a**(i!) (mod N)
        a = moduloPower(a, i, N)

        # computing gcd(a - 1, N)
        d = gcd(a - 1, N)

        if 1 < d < N:
            print('Prime Factorization of', N)
            print('(', d, ',', N // d, ')')
            return True

    # d = 1 or d = N
    return False

if __name__ == '__main__':
    ### "base" for the attack
    a = 2

    ### large prime to factorize
    N = int(sys.argv[1])

    ### "bound" for the attack
    B = int(sys.argv[2])

    if not pollardRhoAttack(a, N, B):
        print(MSG[CODE_FAIL])

