# ---------------------------------------------
# Exercício de Programação 2  - MAP5729 2020
#
# O Algoritmo de Thomas
# 
# Lucas Motta Freire
# ---------------------------------------------


import numpy as np

# Decompoisção LDL^t
def algoritmo_thomas(vec_a, vec_b, vec_c, vec_d):
    '''Parâmetros:
    vec_a = diagonal inferior da matriz
    vec_b = diagnoal da matriz
    vec_c = diagonal superior da matriz
    vec_d = vetor independente do sistema

    Retorna: O vetor diagonal superior e o vetor independente após calcular a decomposição LDL^T'''
    
    c_final = [vec_c[0] / vec_b[0]]
    d_final = [vec_d[0] / vec_b[0]]

    # iterações - eliminação de Gauss
    for i in range(1, len(vec_c) - 1):
        c_n = vec_c[i] / (vec_b[i] - vec_a[i] * c_final[i-1])
        c_final.append(c_n)

    for i in range(1, len(vec_d)):
        d_n = (vec_d[i] - vec_a[i] * d_final[i-1]) / (vec_b[i] - vec_a[i] * c_final[i-1])
        d_final.append(d_n)

    return c_final, d_final
  
  #Substituição de volta

def subst_de_volta(c, d):
    '''Esta função recebe os vetores c, d da decomposição LDL^t realizada pelo algoritmo de Thomas e realiza a substituição
    backward do sistema'''
    
    c_r = c + [0]                   # Acrescentando '0' para trabalhar melhor o índice
    X = [0 for i in range(len(d))]  # Cria um vetor nulo
    X[-1] = d[-1]  + c_r[-1]
    for i in range(2, len(d)+1):
        X[-i] = d[-i] - (c_r[-i]*X[-i+1])

    return X    

# Resolvendo o sistema
def solução_sistema(vec_a, vec_b, vec_c, vec_d):
    '''Esta função recebe os quatro vetores fundamentais do sistema tridiagonal e retorna a solução do sistema'''
    
    c = algoritmo_thomas(vec_a, vec_b, vec_c, vec_d)[0]
    d = algoritmo_thomas(vec_a, vec_b, vec_c, vec_d)[1]

    x = np.array(subst_de_volta(c, d), dtype=FloatingPointError)

    
    return x


def main(n):
    '''Esta função recebe a ordem do sistema a ser resolvido e implementa os
    vetores a(inferior a diagonal), b(diagonal), c(superior a diagonal), d(independete)'''
    a = [0]
    b = []
    c = []
    d = []
    for i in range(n - 1):
        a_dig = float(input("Digite a entrada [" + str(i+1) + "] do vetor abaixo da diag.: "))
        a.append(a_dig)

    for i in range(n):
        b_dig = float(input("Digite a entrada [" + str(i+1) + "] do vetor diag.: "))
        b.append(b_dig)

    for i in range(n - 1):
        c_dig = float(input("Digite a entrada [" + str(i+1) + "] do vetor acima da diag.: "))
        c.append(c_dig)
    c.append(0)

    for i in range(n):
        d_dig = float(input("Digite a entrada [" + str(i+1) + "] do vetor independente: "))
        d.append(d_dig)


    print("X = ", solução_sistema(a, b, c, d))

print("Vamos resolver um sistema tridiagonal através do algoritmo de Thomas")
n = int(input("Digite a ordem do sistema: "))

main(n)

