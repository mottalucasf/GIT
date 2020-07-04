import numpy as np

# Decompoisção LDL^t
def algoritmo_thomas(vec_a, vec_b, vec_c, vec_d):
    '''Parâmetros:
        vec_a = diagonal inferior da matriz;  vec_b = diagnoal da matriz;
        vec_c = diagonal superior da matriz;  vec_d = vetor independente do sistema
    
        Retorna: O vetor diagonal superior e o vetor independente após calcular a decomposição LDL^T'''
    a, b, c, d = np.array(vec_a), np.array(vec_b), np.array(vec_c), np.array(vec_d)
    c_final, d_final = np.zeros(len(c)), np.zeros(len(d))
    
    c_final[0] = c[0] / b[0]
    d_final[0] = d[0] / b[0]

    # iterações - eliminação de Gauss
    for i in range(1, len(c)):
        c_final[i] = c[i] / (b[i] - a[i-1]*c_final[i-1])
        
    for i in range(1, len(d)):
        d_final[i] = (d[i] - a[i-1] * d_final[i-1]) / (b[i] - a[i-1] * c_final[i-1])
    

    return c_final, d_final
  

# Realizando a substituição backward
def subst_de_volta(c, d):
    '''Esta função recebe os vetores c, d da decomposição LDL^t realizada pelo algoritmo de Thomas e realiza a substituição
    backward do sistema'''
    
    x = np.zeros(len(d))
    x[-1] = d[-1]
    for i in range(2, len(d)+1):
        x[-i] = d[-i] - c[-i+1] * x[-i+1]

    return x  

# Resolvendo o sistema
def solução_sistema(vec_a, vec_b, vec_c, vec_d):
    '''Esta função recebe os quatro vetores fundamentais do sistema tridiagonal e retorna a solução do sistema'''
    
    c = algoritmo_thomas(vec_a, vec_b, vec_c, vec_d)[0]
    d = algoritmo_thomas(vec_a, vec_b, vec_c, vec_d)[1]

    x = np.array(subst_de_volta(c, d))

    return x

