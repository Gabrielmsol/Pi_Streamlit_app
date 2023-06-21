from decimal import Decimal as D, getcontext


def Dfac(n):
    h = D('1')
    for i in range(1, n + 1):
        h *= D(str(i))
    return h


def Pi(p, n):
    getcontext().prec = p

    a = D('9801') / D('8').sqrt()
    b = D('26390')
    c = D('1103')
    d = D('396')

    array = [Dfac(i * 4) * (c + b * D(str(i))) / (Dfac(i) ** (4) * d ** (4 * i))
             for i in range(n - 1)]
    s0 = sum(array)
    s = s0 + Dfac((n - 1) * 4) * (c + b * D(str(n - 1))) / (Dfac(n - 1) ** (4) * d ** (4 * (n - 1)))
    pi = a * D('1') / s
    pi2 = D('1') * D('3.1415926535897932384626433832795028841971693993751058209749'
                     '445923078164062862089986280348253421170679821480865132823066'
                     '470938446095505822317253594081284811174502841027019385211055'
                     '596446229489549303819644288109756659334461284756482337867831'
                     '652712019091456485669234603486104543266482133936072602491412'
                     '73724587006606315588')
    print(pi2)
    if p <= 319:
        return pi, 'Error: {:.2E}'.format(pi2 - pi)
    else:
        pi0 = a * D('1') / s0
        return pi, 'Error: {:.2E}'.format(pi - pi0)
