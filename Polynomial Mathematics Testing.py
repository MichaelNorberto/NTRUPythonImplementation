import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy import Symbol,sympify,symbols
import time
########################################################
t0 = time.time()
def random_binning(N, d,return_string=False):
    """
    Function to distribute a sum total of N into d bins
    Returns a list
    """
    import numpy as np
    
    count=N
    sum_count=0
    lst=[]
    for i in range(d-1):
        x=np.random.randint(0,count+1)
        if return_string:
            lst.append(str(x))
        else:
            lst.append(x)
        count=count-x
        sum_count+=x
        
    if return_string:
        lst.append(str(N-sum_count))
    else:
        lst.append(N-sum_count)
    return lst
########################################################
def gen_single_term(lst):
    """
    Function to generate single term from a list of exponents.
    """
    term=''
    for i in range(1,len(lst)+1):
        if lst[i-1]==0:
            pass
        elif lst[i-1]==1:
            term+='x'+str(i)+'.'
        else:
            term+=str(lst[i-1])+'x'+str(i)+'^'+str(i)+'.'
    
    return term[:-1]

print(gen_single_term([1,1,5,4,1]))
t1 = time.time()
total = t1 - t0
print("The total time was: ", total, "s ")
##########################################################
##def count_symbol(lst):
##    syms = set(lst)
##    syms_dict={}
##    term_lst=[]
##    for s in syms:
##        syms_dict[s]=lst.count(s)
##    
##    for k,v in syms_dict.items():
##        if v!=1:
##            term_lst.append(str(v)+'.'+k)
##        else:
##            term_lst.append(k)
##    
##    return term_lst
##########################################################
##t2 = time.time()
##def gen_multinomial(n_features=5,max_power=5,max_terms=10,fixed_terms=None,coefficients=True,
##                   prob_negative_sign=0.3):
##    """
##    Generates multinomial expression.
##    n_features: Number of independent variables
##    max_power: Maximum exponent each terms can be raised to. A random power will be chosen up to this maximum.
##    max_terms: Maximum number of terms. A random number of terms will be chosen up to this maximum.
##    fixed_terms: Attempt will be made to generate only this many terms. Sometimes does not work.
##    coefficients (boolean): Adds (or does not) random integer coefficients in front of the terms.
##    prob_negative_sign: Probability of putting a negative term. 
##                        Each term's sign wil be chosen randomly based on this probability
##    """
##    import numpy as np
##    eqn=''
##    eqn_terms=[]
##    
##    if fixed_terms!=None:
##        n_terms=fixed_terms
##    else:
##        n_terms=np.random.randint(2,max_terms+1)
##    
##    for i in range(n_terms):
##        power=np.random.randint(1,max_power+1)
##        #power=max_power
##        power_lst=random_binning(power,n_features)
##        term=gen_single_term(power_lst)
##        if coefficients:
##            coeff=np.random.randint(1,11)
##            if coeff!=1:
##                coeff=str(coeff)
##                term=coeff+'.'+term
##        eqn_terms.append(term)
##    
##    eqn_terms=count_symbol(eqn_terms)
##    
##    for e in eqn_terms:
##        eqn+=e
##        sign=np.random.choice(['+','-'],p=[prob_negative_sign,1-prob_negative_sign])
##        eqn= eqn+' '+sign+' '
##      
##    return eqn[:-3]
##########################################################
##print(gen_multinomial(coefficients=True))
##t3 = time.time()
##total = t3 - t2
##print("The total time was: ", total, "s ")
##########################################################
##def symbolize(s):
##    """
##    Converts a a string (equation) to a SymPy symbol object
##    """
##    from sympy import sympify
##    s1=s.replace('.','*')
##    s2=s1.replace('^','**')
##    s3=sympify(s2)
##    
##    return(s3)
##########################################################
##def pretty_multinomial(n_features=5,max_power=5,max_terms=10,fixed_terms=None,coefficients=False):
##    from sympy import init_printing
##    init_printing()
##    s=gen_multinomial(n_features=n_features,max_power=max_power,max_terms=max_terms,
##                      fixed_terms=fixed_terms,coefficients=coefficients)
##    sym_s=symbolize(s)
##    return(sym_s)
##########################################################
##def latex_multinomial(n_features=5,max_power=5,max_terms=10,fixed_terms=None,coefficients=False):
##    from sympy import latex
##    s=gen_multinomial(n_features=n_features,max_power=max_power,max_terms=max_terms,
##                      fixed_terms=fixed_terms,coefficients=coefficients)
##    sym_s=symbolize(s)
##    return(latex(sym_s))
##########################################################
##latex_multinomial(coefficients=True,fixed_terms=4)
##########################################################
##lst=[]
##for i in range(6):
##    lst.append(pretty_multinomial(coefficients=True))
##lst
##########################################################
##pretty_multinomial(n_features=2,max_power=4,coefficients=True)
##
