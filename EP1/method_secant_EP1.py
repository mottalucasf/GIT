#Tentativa de implementação do método da Secante.

# Definir a função:

import math

def secant(f, x0, x1, epsilon, maxiter = 50):
    if math.fabs(f(x0))<=epsilon:
        return x0
    elif math.fabs(f(x1))<=epsilon:
        return x1
    print("k \t x0 \t\t f(x0) \t\t f(x1)")
    k=1
    while k<=maxiter:
        x2=x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        print ("%d \t %e \t %e"%(k,x2,f(x2)))
        if math.fabs(f(x2))<=epsilon:
            return x2
        x0=x1
        x1=x2
        k=k+1
    print("Erro : Número máximo de interações atingido")
    return x2
if __name__ == "__main__":
    def f(x):
        return x**2-2

raiz = secant(f, 1, 2, 0.0001)
print(raiz)
