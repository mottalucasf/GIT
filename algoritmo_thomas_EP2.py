# Tentativa de implementação do Algoritmo de Thomas


def subst_de_volta(c, d):
    '''Esta função recebe os vetores c, d do alg. de Thomas e faz a substituição
    backward no sistema'''
    #Substituição de volta
    c_r = c + [0]                   # Acrescentando '0' pra traalhar melhor o índice
    X = [0 for i in range(len(d))]  # Cria um vetor nulo
    X[-1] = d[-1]  + c_r[-1]
    for i in range(2, len(d)+1):
        X[-i] = d[-i] - (c_r[-i]*X[-i+1])

    return X    
        
        

def algoritmo_thomas(a, b, vector_c, vector_d):
    '''Esta função recebe o vetor acima da diagonal principal da matriz
    tridiagonal denotado por 'vector_c e o vetor independete do sistema referente
    denotado por vector_d e retorna os mesmos tranformados pela eliminação Gaussiana'''
    
    c_final = [vector_c[0] / b[0]]
    d_final = [vector_d[0] / b[0]]

    # iterações eliminação de Gauss
    for i in range(1, len(vector_c)-1):
        c_n = vector_c[i] / (b[i] - a[i]*c_final[i-1])
        c_final.append(c_n)

    for i in range(1, len(vector_d)):
        d_n = (vector_d[i] - a[i]*d_final[i-1]) / (b[i] - a[i]*c_final[i-1])
        d_final.append(d_n)

    return c_final, d_final


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

    c_final, d_final = algoritmo_thomas(a, b, c, d)
    print("X = ", subst_de_volta(c_final, d_final))

print("Vamos resolver um sistema tridiagonal")
n = int(input("Digite a ordem do sistema: "))

main(n)

