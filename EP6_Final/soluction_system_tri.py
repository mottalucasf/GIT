import numpy as np
import integration as intg



# LDL Decomposition ^ t of the System
def algoritmo_thomas(vec_a, vec_b, vec_c, vec_d):
    '''Parameters:
        vec_a = bottom diagonal of the matrix;  vec_b = diagnoal of the matrix;
        vec_c = top diagonal of the matrix;  vec_d = system independent vector
    
        Return: The top diagonal vector and the independent vector after calculating the LDL ^ T decomposition'''
    a, b, c, d = np.array(vec_a), np.array(vec_b), np.array(vec_c), np.array(vec_d)
    c_final, d_final = np.zeros(len(c)), np.zeros(len(d))
    
    c_final[0] = c[0] / b[0]
    d_final[0] = d[0] / b[0]

    # iterations - Gaussian elimination
    for i in range(1, len(c)):
        c_final[i] = c[i] / (b[i] - a[i-1]*c_final[i-1])
        
    for i in range(1, len(d)):
        d_final[i] = (d[i] - a[i-1] * d_final[i-1]) / (b[i] - a[i-1] * c_final[i-1])
    

    return c_final, d_final


#Performing backward replacement
def subst_de_volta(c, d):
    '''This function receives the vectors c, d from the LDL ^ t decomposition performed by the Thomas algorithm and performs the substitution
    system backward'''
    
    x = np.zeros(len(d))
    x[-1] = d[-1]
    for i in range(2, len(d)+1):
        x[-i] = d[-i] - c[-i+1] * x[-i+1]

    return x  


# Solving the system
def solução_sistema(vec_a, vec_b, vec_c, vec_d):
    '''This function receives the four fundamental vectors of the tridiagonal system and returns the system solution'''
    
    c = algoritmo_thomas(vec_a, vec_b, vec_c, vec_d)[0]
    d = algoritmo_thomas(vec_a, vec_b, vec_c, vec_d)[1]

    x = np.array(subst_de_volta(c, d))

    return x
