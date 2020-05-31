# Esta é uma tentativa de implementação do método iterativo de Jacobi
import numpy as np
def itera_jacobi(A, b, n_iter):
    '''Esta função é responsável por introduzir o método iterativo de Jacobi para uma matriz
    com n_iter iterações'''

    n = A.shape[0] # Número de linhas da matriz
    D = np.diag(A) #Diagonal da matriz
    L_U = A - np.diag(D)   # L + U
    
    x = np.zeros(n)
    s = np.zeros((n, n_iter))
    
    for k in range(n_iter):
        x = (b - L_U.dot(x)) / D  #iterações de Jacobi, array.dot multiplica arrays
        s[:, k] = x               #guarda a k-ésima iteração na voluna k de s

    return s

if __name__=="__main__":
    A = np.array([[10, -1, 2, 0],[-1, 11, -1, 3],[2, -1, 10, -4],[0, 3, -1, 8]])
    b = np.array([6, 25, -11, 15])
    n_iter = 7

print(itera_jacobi(A, b, n_iter))
print()