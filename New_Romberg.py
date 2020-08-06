#------------------------
# Romberg Method
#
# Lucas Motta Freire
#------------------------

import numpy as np
import time as tm

inicio = tm.time()

# Function
def f(x):
    return 1/(1-x)

# Interval
a, b = 0, 0.995

# Tolerance
epsilon = 1.0e-12
MaxIter = 6

def trapz(a, b, f, t, i):
    '''Parameters: 
        a, b : Points Extrems;   f : integral function
        t : Value of T(h_i-1);   i : index
        
        Return: Value of T(h_i)'''
    if i==0:
        t = (b-a)/2*(f(a)+f(b))
    else:    
        hi = (b-a)/2**i                                           
        new_points = np.linspace(a + hi, b - hi, 2**(i-1))        # New points next step
        t = 0.5 * t + hi * np.sum(f(new_points))                  # Recalculating trapezium

    return t


def romberg(a, b, epsilon, MaxIter, f):
    '''Parameters: 
        a, b : Points Extrems;   epsilon, MaxIter : Tolerance
        f : integral function        
        Return: Romberg Table; Tnn - Integral Value; Romberg Table Dimension; If converges'''
    convergence = True
    TR = np.zeros((MaxIter, MaxIter), dtype=float)
    TR[0,0] = trapz(a, b, f, 0, 0)
    
    for i in range(1, MaxIter):                                                     # building the table
        TR[i, 0] = trapz(a, b, f, TR[i-1,0], i)                                     # First Column
        for k in range(1, i+1):                                                     # i-th row                                            
            TR[i, k] = (4**k * TR[i, k-1] - TR[i-1, k-1])/(4**k - 1)
        
        if np.abs(TR[i,k] - TR[i, k-1]) <=  epsilon * np.abs(TR[i,k]):              # Relative Variation; Stopping Criteria
            break
    
    if np.abs(TR[i,k] - TR[i, k-1]) >  epsilon * np.abs(TR[i,k]):
        convergence = False

    return TR[:i+1,:k+1], TR[i, k], k+1, convergence

Table = romberg(a, b, epsilon, MaxIter, f)[0]
print(Table)
print()
print()


def new_line(a, b, epsilon, MaxIter, f, Table,l):
    n = len(Table)
    last_row = Table[n-1:n, :MaxIter]                       # Last Row
    new_line = np.zeros(n)
    new_line[0] = trapz(a, b, f, last_row[0], (n-1) + l)
    for i in range(1,n):
        new_line[i] = (4**i * new_line[i-1] - last_row[i-1])/(4**i - 1)

    return new_line


print(new_line(a, b, epsilon, MaxIter, f, Table,1))


""" def new_table(a, b, epsilon, MaxIter, f, Table, l):
    TR = np.zeros((MaxIter, MaxIter), dtype=float)
    TR[0,0] = Table[l % 6,0]
    
    for i in range(1, MaxIter):                                                     # building the table
        TR[i, 0] = trapz(a, b, f, TR[i-1,0], i+l)
        for k in range(1, i+1):
            TR[i, k] = (4**k * TR[i, k-1] - TR[i-1, k-1])/(4**k - 1)
                       # Maximum iterations reached
            
    return TR




print(new_table(a, b, epsilon, MaxIter, f, Table, 1)) """
""" ef romb_integrate(a, b, epsilon, MaxIter, f):
    if romber_converg_1:
        value = romberg(a, b, epsilon, MaxIter, f)[1]
        iterations = romberg(a, b, epsilon, MaxIter, f)[2]
        return value, iterations
    
    else:
        for i in range(1,6):
            ti = remake_romberg(a, b, epsilon, MaxIter, f, i)
            print(ti[0])
            print()
            print(i)
            if ti[3]:
                break
        value = remake_romberg(a, b, epsilon, MaxIter, f, i)[1]
        iterations1 = remake_romberg(a, b, epsilon, MaxIter, f, i)[2]

        return value, iterations1
 """


fim = tm.time()
t_trapz = fim - inicio
print(t_trapz)


