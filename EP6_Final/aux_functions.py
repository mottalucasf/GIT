import numpy as np

def phi(x, i, n):
    '''Parameters:
    x : variable
    i : respective index the phi function
    n : Partition dimension
    
    Retorna: The value of the i-th hat function calculated at x'''
    h = 1 / (n+1)
    knot = np.linspace(0, 1, n+2)                       
    phi_x = 0
    
    if  knot[i-1] <= x <= knot[i]:
        phi_x = (x - knot[i-1])/h
    elif knot[i] <= x <= knot[i+1]:
        phi_x = (knot[i+1] - x)/h

    return phi_x

def phi_vector(x, n):
    '''Parameters:
    x : variable
     n : Dimensão da partição
    
    Return : vector of dimension "n" whose i-th input is given by the value of the i-th hat function in y'''
    phi_vec = np.zeros(n)
    for i in range(n):
        phi_vec[i] = phi(x, i+1, n)
    return phi_vec

def erro_infi(v_a, v_b):
    '''Parameters:
    vec_a, vec_b : vectors

    Return: The error value between the respective vectors and the infinite norm '''
    v_a = np.array(v_a)             # Convertendo para array tipo numpy///
    v_b = np.array(v_b)
    v = np.abs(v_a - v_b)           # calculando o módulo do vetor diferença
    return max(v)
