#----------------------------------
# Exercício 1 - EP4
#
# Lucas Motta Freire
#---------------------------------

import Rayleigh_Ritz as ryrz # Módulo para utilizar o método de Rayleigh_Ritz na resolução do exercício
import numpy as np
import time
import matplotlib.pyplot as plt


#Parâmetros do exercício, caso necessário, implementar para input
a , b, lamb = 0, 1, 0


#-------------------------------------------
# Funções específicas para este exercício
#-------------------------------------------


# Solução exata do problema
def solução_exata(x):
    return 0.5 * x * (1 -x)


# Implementando o vetor d para f(x)=1
def vector_d(a, b, n):
    '''Parâmetros
    a = Extremo inicial do intervalo; b = Extremo final do intervalo; n = Qtd de pontos internos da partição
    
    Retorna: O vetor independente do sistema normal'''
    
    vector_d = np.zeros(n)
    for i in range(n):
        vector_d[i] = (b-a) / (n+1)
    
    return vector_d


# Implementando a função u_barra
def u_barra(y, n, a, b, lamb):
    '''Função que calcula u_barra(solução numérica) dependente de n, em um certo valor y'''
    c = ryrz.vector_minimizador(a, b, lamb, n, vector_d(a, b, n))          # Alocando o vetor minimizador    
    fi = ryrz.phi_vector(y, a, b, n)                                            # Array: fi[i] = phi[i](y) 
    return np.dot(c, fi)


# Implementando a função erro sobre os nós pela norma infinita
def erro_nós(a, b, lamb, n):
    '''Esta função recebe os parêmetros do intervalo, da partição, valor de lambda e o valor de n e calcula o erro
    entre a solução exata e a solução numérica aplicada sobre os nós'''
    nós = np.linspace(a, b, n+2)                                           # Gerando nós igualmente espaçados
    u_aprox, u_exato = np.zeros(n), np.zeros(n)             
    
    for i in range(n):
        u_exato[i] = solução_exata(nós[i])
        u_aprox[i] = u_barra(nós[i], n, a, b, lamb)
    
    return ryrz.erro_infi(u_exato, u_aprox)



start_time = time.time()
# Leitura do programa
print('Vamos analisar o erro entre a solução exata e a solução aproximada do Exercício 1.')
print()
print('Ao final o código retorna:')
print('* Uma tabela que realciona o valor de n com o erro sobre os nós')
print('* Uma comparação gráfica entre a solução exata e a solução aproximada da EDO')
print('* O tempo de execução do programa')



# Analisando o erro sobre os nós
n = [15,31,63,127,255]
erros = []
for x in n:
    erros.append(erro_nós(a, b, lamb, n = x))

print('Valor de n', ' '*20, 'Erro')
for x in n:
    print(x, ' '*20, erro_nós(a, b, lamb, n = x))



#-----------------------------------------------------------
# Plotando o gráfico de u_barra com relação a solução exata
#-----------------------------------------------------------
x = np.linspace(0, 1, 100)                                       # Gerando valores igualmente espaçados no intervalo [0,1]

y_1 = np.zeros(100)
for i in range(100):
    y_1[i] = u_barra(x[i], 255, a, b, lamb)                      # Guardando os valores de u_barra no intervalo [0,1] em uma lista


# Plotando o gráfico da u_barra em comparação com a solução exata
plt.subplot(1, 2, 1)                                             # Configurando o primeiro gráfico
plt.plot(x , y_1, color='r')
plt.title('Gráfico da solução numérica')

plt.subplot(1, 2, 2)                                             # Configurando o segundo gráfico
plt.plot(x, solução_exata(x))
plt.title('Gráfico da solução exata')

elapsed_time = time.time() - start_time
print()
print("  Tempo de execucao: "+str(elapsed_time)+" segundos")

plt.show()