# Esta é uma tentativa de analisar o método de Newton via programação em python

# Definir uma função
import math

def newton(f, flin, x0, epsilon, maxIter=50):
    if math.fabs(f(x0))<= epsilon:
        return x0
    print("k\t x0\t\t f(x0)")
    k=1
    while k<=maxIter:
        x1=x0-f(x0)/flin(x0)
        print("%d\t%e\t%e"%(k,x1,f(x1)))
        if math.fabs(f(x1))<= epsilon:
            return x1
        x0 = x1
        k = k+1
    print("ERRO:Número máximo de interações atingido")
    return x1
if __name__ == "__main__":
    def f(x):
        return 5*x**5 - 2*x**4 + 3*x**2 - 8*x - 10
    def flin(x):
        return 25*x**4 - 8*x**3 + 6*x - 8
raiz = newton(f, flin, 1.5, 0.001)
print(raiz)