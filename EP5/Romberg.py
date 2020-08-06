#------------------------
# Romberg Method
#
# Lucas Motta Freire
#------------------------

import numpy as np
import time as tm

start = tm.time()

# Function
def f(x):
    return 1/(1+x**2)
f_x = '1/(1+x**2)'
# Interval
a, b = -5, 5

# Tolerance
epsilon = 1.0e-8
MaxIter = 50

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
        Return: Romberg Table in array and a bollian value for the convergence of the method'''
    convergence = True
    TR = np.zeros((MaxIter, MaxIter), dtype=float)
    TR[0,0] = trapz(a, b, f, 0, 0)
    
    for i in range(1, MaxIter):                                                     # building the table in array format
        TR[i, 0] = trapz(a, b, f, TR[i-1,0], i)
        for k in range(1, i+1):
            TR[i, k] = (4**k * TR[i, k-1] - TR[i-1, k-1])/(4**k - 1)
        if np.abs(TR[i,k] - TR[i, k-1]) <=  epsilon * np.abs(TR[i,k]):              # Relative Variation
            break
    
    if np.abs(TR[i,k] - TR[i, k-1]) >  epsilon * np.abs(TR[i,k]):                   # Maximum iterations reached
        convergence = False
    
    return TR[:i+1,:k+1], convergence



def integral(a, b, epsilon, MaxIter, f):
    '''Parameters: 
        a, b : Points Extrems;   epsilon, MaxIter : Tolerance
        f : integral function        
        Return: Romberg Table and the approximation of the value of the integral if Romberg converges'''
    table = romberg(a, b, epsilon, MaxIter, f)[0]
    n = len(table)
    romber_converg_1 = romberg(a, b, epsilon, MaxIter, f)[1]
    if romber_converg_1:
        print('Step \t StepSize \t Results')
        for i in range(n):
            print('%d \t %f \t'  % (2**i, 1/2**i), end="")
            for k in range(i+1):
                print(' %f \t' % table[i,k], end="")
            print()
        print()
        print('The approximate value of the integral is', table[n-1,n-1], 'with', n, 'iterations/rows')
        print()
    else:
        print("Romberg's method exceeded", MaxIter ,"lines")

print('Approximating the value of \int_{',a,'}{',b,'}[',f_x,'] by Romberg')
integral(a, b, epsilon, MaxIter, f)

end = tm.time()
time_trapz = end - start
print("Tempo de Execução", time_trapz)


