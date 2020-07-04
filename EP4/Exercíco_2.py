#----------------------------------
# Exercício 2 - EP4
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
    return x**2 * ((x-1)**2)


# Implementando o vetor d, para f(x)=12x(1-x) - 2, utilizando a função g, tal que g'' = f
def g(x):
    return 2*(x**3) - x**4 - x**2

def vector_d(a, b, n):                                           # A Partir desta linhas o código é comum entre os exercícios
    '''Parâmetros
    a = Extremo inicial do intervalo
    b = Extremo final do intervalo
    n = Qtd de pontos internos da partição
    
    Retorna: O vetor independente do sistema normal'''
    nós, h = np.linspace(a, b, n+2), (b-a) / (n+1)
    vector_d = np.zeros(n)
    for i in range(n):
        vector_d[i] = 1/h * ( g(nós[i+2]) - 2*g(nós[i+1]) + g(nós[i]) ) 
    
    return vector_d


# Implementando a função u_barra
def u_barra(y, n, a, b, lamb):
    '''Função que calcula u_barra dependente de n, em um certo valor y'''
    c = ryrz.vector_minimizador(a, b, lamb, n, vector_d(a, b, n))
    fi = ryrz.phi_vector(y, a, b, n)
    return np.dot(c, fi)


# Implementando a função erro sob
def erro_entre_nós(a, b, lamb, n):
    '''Esta função recebe os parêmetros do intervalo, da partição, valor de lambda e o valor de n e calcula o erro
    entre a solução exata sobre os pontos da partição e a solução numérica'''
    partição = np.linspace(a, b, 10*n + 1)                            # Gerando valores igualmente espaçados no intervalo [0,1]                                         # Guardando os pontos interiores da partição em um array
    u_aprox = np.zeros(10*n + 1)             
    u_exato = np.zeros(10*n + 1)
    
    for i in range(10*n + 1):
        u_exato[i] = solução_exata(partição[i])
        u_aprox[i] = u_barra(partição[i], n, a, b, lamb)
    
    return ryrz.erro_infi(u_exato, u_aprox)


# Função para analisar velocidade do erro
def converg_entre_nós(n):
    erro_n = erro_entre_nós(a, b, lamb, n)
    return erro_n * ((n+1)/(b-a))**2


# Implementando a função erro sobre a norma infinita sobre os nós
def erro_nós(a, b, lamb, n):
    '''Esta função recebe os parêmetros do intervalo, da partição, valor de lambda e o valor de n e calcula o erro
    entre a solução exata sobre os pontos da partição e a solução numérica'''
    nós = np.linspace(a, b, n+2)                            # Gerando valores igualmente espaçados no intervalo [0,1]                                         # Guardando os pontos interiores da partição em um array
    u_aprox = np.zeros(n+2)           
    u_exato = np.zeros(n+2)
    
    for i in range(n+2):
        u_exato[i] = solução_exata(nós[i])
        u_aprox[i] = u_barra(nós[i], n, a, b, lamb)
    
    return ryrz.erro_infi(u_exato, u_aprox)


# Função para analisar velocidade do erro sobre os nós
def converg_nós(n):
    erro_n = erro_nós(a, b, lamb, n)
    return erro_n * ((n+1)/(b-a))**2




start_time = time.time()
# Leitura do programa
print('Vamos analisar o erro entre a solução exata e a solução aproximada do Exercício 2.')
print('Ao final o código retorna:')
print()
print('* Uma tabela que relaciona o valor de n, o erro e a comparação entre o erro e h**2 entre os nós')
print('* Uma tabela que relaciona o valor de n e o erro sobre os nós')
print('* Uma comparação gráfica entre a solução exata e a solução aproximada da EDO')
print('* O tempo de execução do programa')
print()



#----------------------------------------------- 
# Analisando o erro e a taxa de convergência
#----------------------------------------------
# Criando os eixos de comparação
n = [15,31,63,127,255]
erro_entre = []
erro_sobre = []
for x in n:
    erro_entre.append(erro_entre_nós(a, b, lamb, n = x))
    erro_sobre.append(erro_nós(a, b, lamb, n = x))


#Imprimindo a tabela de comparação do erro entre os nós
 
print('Tabela de comparação do erro entre os nós')
print('n', ' '*14, 'h', ' '*20, 'erro', ' '*24, 'erro/h^2')
for x in n:
    print(x, ' '*10, (b-a)/(x+1), ' '*10, erro_entre_nós(a, b, lamb, n = x), ' '*10,  converg_entre_nós(x))

print()
#Imprimindo a tabela de comparação do erro sobre os nós

print('Tabela de comparação do erro sobre os nós')
print('n', ' '*14, 'h', ' '*20, 'erro', ' '*24, 'erro/h^2')
for x in n:
    print(x, ' '*10, (b-a)/(x+1), ' '*10, erro_nós(a, b, lamb, n = x), ' '*10,  converg_nós(x))



#-----------------------------------------------------------
# Plotando o gráfico de u_barra com relação a solução exata
#-----------------------------------------------------------

#Criando os eixos para o gráfio

x = np.linspace(a, b, 100)                                      # Gerando valores igualmente espaçados no intervalo [0,1]

y_1 = np.zeros(100)
for i in range(100):
    y_1[i] = u_barra(x[i], 255, a, b, lamb)                     # Guardando os valores de u_barra no intervalo [0,1] em uma lista


# Plotando os gráficos
 
plt.subplot(1, 2, 1)
plt.plot(x , y_1, color='r')
plt.title('Gráfico da solução numérica')

plt.subplot(1, 2, 2)
plt.plot(x, solução_exata(x))
plt.title('Gráfico da solução exata')


#Plotando o gráfico do erro
""" 
plt.plot(n, erro_entre, 'r--')
plt.yscale('log')
plt.title('Erro em função de n, entre os nós')
 """
#Marcando o tempo de execução da rotina

elapsed_time = time.time() - start_time
print()
print("  Tempo de execucao: "+str(elapsed_time)+" segundos")

plt.show()