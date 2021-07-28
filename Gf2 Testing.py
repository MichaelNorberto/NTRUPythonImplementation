  
import numpy as np


def strip_zeros(a):
    """Strip un-necessary leading (rightmost) zeroes
    from a polynomial"""

    return np.trim_zeros(a, trim='b')


def check_type(a, b):
    """Type check and force cast to uint8 ndarray
    Notes
    -----
    Ideally for best performance one should always use uint8 or bool when using this library.
    """

    if isinstance(a, np.ndarray):
        a = np.array(a, dtype="uint8")
    if isinstance(b, np.ndarray):
        b = np.array(b, dtype="uint8")

    if a.dtype is not "uint8":
        a = a.astype("uint8")

    if b.dtype is not "uint8":
        b = b.astype("uint8")

    return a, b


def padding(a, dim):
    """Zero-pad input array a a to length dim, zeroes are appended at the right"""

    return np.pad(a, (0, dim-len(a)), 'constant', constant_values=(0))


def to_same_dim(a, b):
    """Given two arrays a and b returns the two arrays with the shorter zero-padded to have
    the same dimension of the longer. The arrays are padded with zeroes appended to the right.
    """

    if len(a) > len(b):
       return a, padding(b, len(a))

    elif len(a) < len(b):
        return padding(a, len(b)), b

    else:
        return a, b


def zeros(dim):
    """Returns dim coefficients for -1 degree polynomial"""

    return np.zeros(dim, dtype='uint8')


def zerodegree_pol(dim):
    """Returns dim coefficients for a zero degree polynomial"""

    out = zeros(dim)
    out[0] = 1

    return out

#############################################################################################
def xor(a, b):
    """Computes the element-wise XOR of two ndarrays"""

    return np.logical_xor(a, b, dtype='uint8').astype("uint8")




def gf2_add(a, b):

    """Add two polynomials in GF(p)[x]
    Parameters
    ----------
    a : ndarray (uint8 or uint8) or list
        Addend polynomial's coefficients.
    b : ndarray (uint8 or uint8) or list
        Addend polynomial's coefficients.
    Returns
    -------
    q : ndarray of uint8
        Resulting polynomial's coefficients.
    Notes
    -----
    Rightmost element in the arrays is the leading coefficient of the polynomial.
    In other words, the ordering for the coefficients of the polynomials is like the one used in MATLAB while
    in Sympy, for example, the leftmost element is the leading coefficient.
    Examples
    ========
    >>> a = np.array([1,0,1], dtype="uint8")
    >>> b = np.array([1,1], dtype="uint8")
    >>> gf2_add(a,b)
    array([0, 1, 1], dtype=uint8)
"""
    a, b = check_type(a, b)

    a, b = strip_zeros(a), strip_zeros(b)

    N = len(a)

    D = len(b)

    if N == D:
        res = xor(a, b)

    elif N > D:

        res = np.concatenate((xor(a[:D], b), a[D:]))

    else:

        res = np.concatenate((xor(a, b[:N]), b[N:]))

    return strip_zeros(res)
############################################################################################
def gf2_div(dividend, divisor):
    """This function implements polynomial division over GF2.
    Given univariate polynomials ``dividend`` and ``divisor`` with coefficients in GF2,
    returns polynomials ``q`` and ``r``
    (quotient and remainder) such that ``f = q*g + r`` (operations are intended for polynomials in GF2).
    The input arrays are the coefficients (including any coefficients
    equal to zero) of the dividend and "denominator
    divisor polynomials, respectively.
    This function was created by heavy modification of numpy.polydiv.
    Parameters
    ----------
    dividend : ndarray (uint8 or bool)
        Dividend polynomial's coefficients.
    divisor : ndarray (uint8 or bool)
        Divisor polynomial's coefficients.
    Returns
    -------
    q : ndarray of uint8
        Quotient polynomial's coefficients.
    r : ndarray of uint8
        Quotient polynomial's coefficients.
    Notes
    -----
    Rightmost element in the arrays is the leading coefficient of the polynomial.
    In other words, the ordering for the coefficients of the polynomials is like the one used in MATLAB while
    in Sympy, for example, the leftmost element is the leading coefficient.
    Examples
    ========
    >>> x = np.array([1, 0, 1, 1, 1, 0, 1], dtype="uint8")
    >>> y = np.array([1, 1, 1], dtype="uint8")
    >>> gf2_div(x, y)
    (array([1, 1, 1, 1, 1], dtype=uint8), array([], dtype=uint8))
    """

    N = len(dividend) - 1
    D = len(divisor) - 1

    if dividend[N] == 0 or divisor[D] == 0:
        dividend, divisor = strip_zeros(dividend), strip_zeros(divisor)

    if not divisor.any():  # if every element is zero
        raise ZeroDivisionError("polynomial division")
    elif D > N:
        q = np.array([])
        return q, dividend

    else:
        u = dividend.astype("uint8")
        v = divisor.astype("uint8")

        m = len(u) - 1
        n = len(v) - 1
        scale = v[n].astype("uint8")
        q = np.zeros((max(m - n + 1, 1),), u.dtype)
        r = u.astype(u.dtype)

        for k in range(0, m - n + 1):
            d = scale and r[m - k].astype("uint8")
            q[-1 - k] = d
            r[m - k - n:m - k + 1] = np.logical_xor(r[m - k - n:m - k + 1], np.logical_and(d, v))

        r = strip_zeros(r)

    return q, r
################################################################################################
def gf2_inv(f, g):
    """ Given a polynomial ``f`` and an irriducible polynomial ``g`` both in GF(p)[x], computes the
        multiplicative inverse ``out``, such that f*out == 1 mod(g) (All operations are intended in GF(p)[x]).
        Parameters
        ----------
        f : ndarray (uint8 or bool) or list
            Input polynomial's coefficients.
        g : ndarray (uint8 or bool) or list
            Irriducible polynomial's coefficients.
        Returns
        -------
        out : ndarray of uint8
            Multiplicative inverse polynomial's coefficients.
        Notes
        -----
        Rightmost element in the arrays is the leading coefficient of the polynomial.
        In other words, the ordering for the coefficients of the polynomials is like the one used in MATLAB while
        in Sympy, for example, the leftmost element is the leading coefficient.
        Examples
        ========
        >>> x = np.array([1, 1, 0, 1], dtype="uint8")
        >>> y = np.array([1, 0, 0, 0, 0, 1], dtype="uint8")
        >>> gf2_inv(x,y)
        array([0, 1, 1, 1], dtype=uint8)
        """

    out = gf2_xgcd(f, g)[0]

    return out


def gf2_xgcd(b, a):
    """Perform Extended Euclidean Algorithm over GF2
    Given polynomials ``b`` and ``a`` in ``GF(p)[x]``, computes polynomials
    ``s``, ``t`` and ``h``, such that ``h = gcd(f, g)`` and ``s*b + t*a = h``.
    The typical application of EEA is solving polynomial diophantine equations and findining multiplicative inverse.
    Parameters
    ----------
    b : ndarray (uint8 or bool) or list
        b polynomial's coefficients.
    a : ndarray (uint8 or bool) or list
        a polynomial's coefficients.
    Returns
    -------
    y2 : ndarray of uint8
         s polynomial's coefficients.
    x2 : ndarray of uint8
         t polynomial's coefficients.
    b : ndarray of uint8
        h polynomial's coefficients.
    Notes
    -----
    Rightmost element in the arrays is the leading coefficient of the polynomial.
    In other words, the ordering for the coefficients of the polynomials is like the one used in MATLAB while
    in Sympy, for example, the leftmost element is the leading coefficient.
    Examples
    ========
    >>> x = np.array([1, 1, 1, 1, 1, 0, 1, 0, 1], dtype="uint8")
    >>> y = np.array([1, 0, 1], dtype="uint8")
    >>> gf2_xgcd(x,y)
    (array([0, 1, 1, 1], dtype=uint8),
     array([1, 1], dtype=uint8),
     array([1], dtype=uint8))
    """

    x1 = np.array([1], dtype="uint8")
    y0 = np.array([1], dtype="uint8")

    x0 = np.array([], dtype="uint8")
    y1 = np.array([], dtype="uint8")

    while True:

        q, r = gf2_div(b, a)

        b = a

        if not r.any():
            break

        a = r

        if not (q.any() and x1.any()):  # if q is zero or x1 is zero
            x2 = x0
        elif not x0.any():  # if x0 is zero
            x2 = mul(x1, q)
        else:
            mulres = mul(x1, q)

            x2 = gf2_add(x0, mulres)

        if not (q.any() and y1.any()):
            y2 = y0
        elif not y0.any():
            y2 = mul(y1, q)
        else:
            mulres = mul(y1, q)

            y2 = gf2_add(y0, mulres)

        # update
        y0 = y1
        x0 = x1
        y1 = y2
        x1 = x2

    return y2, x2, b


def mul(a, b):
    """Performs polynomial multiplication over GF2.
       Parameters
       ----------
       b : ndarray (uint8 or bool) or list
           Multiplicand polynomial's coefficients.
       a : ndarray (uint8 or bool) or list
           Multiplier polynomial's coefficients.
       Returns
       -------
       out : ndarray of uint8
       Notes
       -----
       This function performs exactly the same operation as gf2_mul but here instead of the fft, convolution
       in time domain is used. This is because this function must be used multiple times in gf2_xgcd and performing the
       fft in that instance introduced significant overhead.
    """

    out = np.mod(np.convolve(a, b), 2).astype("uint8")

    return strip_zeros(out)

##########################################################################################
