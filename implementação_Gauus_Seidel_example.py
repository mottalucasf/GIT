import numpy as np


def iteração_g_s(A, b, x0):
    '''Esta função recebe a matriz dos coeficentes, o vetor independente
    e um chute inicial e calcula uma iteração de Gauus Seidel'''
    
    n = A.shape[0] # Guardando a ordem do sistema
    D = np.diag(A) # Guardando a diagonal de A
    A_D = A - np.diag(D) # Gerando a matriz L + U
    x = x0

    for i in range(n):
        x[i] = (1 / D[i]) * (b[i] - np.dot(A_D[i, :], x))    # fazendo a iteração de Gauss Seidel
    return x                                                 # utilizando a matriz L+U para iterar
                                                            # np.dot é utilizado para multiplicar array

def gauus_seidel(A, b, x0, n_iter):
    '''Esta função recebe a matriz dos coeficientes, o vetor independente
    , um chute inicial e o número de iterações (k) e realiza k iterações de Gauss Seidel'''
    n = A.shape[0]
    s = np.zeros((n, n_iter))
    x = x0
    
    for k in range(n_iter):                               # Guardando as iterações nas colunas da matriz s
        x = iteração_g_s(A, b, x)
        s[:, k] = x
    return s

if __name__=="__main__":           #Exemplo prático de aplicação
    A = np.array([[10, -1, 2, 0],[-1, 11, -1, 3],[2, -1, 10, -4],[0, 3, -1, 8]])
    b = np.array([6, 25, -11, 15])
    x0 = np.zeros(4)
    n_iter = 5


print(gauus_seidel(A, b, x0, n_iter))
