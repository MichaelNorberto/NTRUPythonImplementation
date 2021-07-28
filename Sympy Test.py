import sympy as sym
from sympy import GF

def make_poly(N, coeffs):

    x = sym.Symbol('x')
    coeffs = list(reversed(coeffs))
    y = 0
    if len(coeffs) < N:
        for i in range(len(coeffs)):
            y += (x**i)*coeffs[i]
        y = sym.poly(y)
        return y
    else:
        for i in range(N):
            y += (x**i)*coeffs[i]
        y = sym.poly(y)
        return y

N = 11
p = 3
q =257

f = [-1,0,-1,0,-1,0,1,0,1,1,1]
g = [-1,-1,0,-1,0,1,0,1,0,1]
m = [1,0,0,-1,-1,0,1,1]
r = [-1,0,0,1,0,0,1,-1,0,0,1]

f_poly = make_poly(N,f)
g_poly = make_poly(N,g)
m_poly = make_poly(N,m)
r_poly = make_poly(N,r)


x = sym.Symbol('x')

Fp = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(p, symmetric = False))
Fq = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(q, symmetric = False))

print('\nf =',f_poly)
print('\nFp =',Fp)
print('\nFq =',Fq)
print("\ng = ", g_poly)
print("\nr=", r_poly)
print("\nm=", m_poly)
print("\n===============================================")
h = p*((Fq.mul(g_poly)))

h = sym.polys.polytools.trunc(h, q)
#h = sym.polys.polytools.div(h, x**N -1)

print("\nPublic Key = ", h)

e = r_poly.mul(h) + m_poly
e = sym.polys.polytools.trunc(e, q)
print("\nThe Encrypted Message is: ", e)

a = f_poly.mul(e)
print("\na = ", a)
b = sym.polys.polytools.trunc(a,p)
print("\nb = ", b)
c = sym.polys.polytools.trunc(m_poly, p)
print("\nThe Original Message is: ", c)

print(c.all_coeffs())
