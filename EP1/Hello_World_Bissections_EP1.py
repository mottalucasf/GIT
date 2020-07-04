# Este é o meu primeiro arquivo utilizando o GIT

# Tenho que elaborar um método para encontrar as raízes de uma equação do tipo f(X)=0

#Importar a biblioteca matemática

import math

# Definir um intervalo [a,b]
a = 1
b = 2
e=0.00001

#Definir uma função

def f(x):
    return x**2-2

# Teste do teorema de Bolzano
if f(a)*f(b)<0:
    while (math.fabs(b-a)/2 > e):    # Criando um laço
        xi=(a+b)/2                   
        if f(xi) == 0:
            print("A Raiz é:" ,xi)
            break
        else:
            if f(a)*f(xi) < 0:
                b = xi
            else:
                a = xi
    print("O Valor da raiz é:", xi)
else:
    print("não há raiz neste intervalo")

