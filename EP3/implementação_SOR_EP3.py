# implementação do método iterativo SOR para o EP3.
import matplotlib.pyplot as plt    # Para plotar gráficos
import math                        # Para trabalhar com funções matemáticas
import numpy as np                 # Para trabalhar com matrizes
import random                      # Para gerar números aleatórios
 
def matriz_temperatura(n, t0):
    '''Esta função recebe o valor de n e um chute inicial e cria a matriz
    temperatura inicial de dimensão n+1'''
    T = np.zeros((n+1, n+1))

    for i in range(n+1): # criando as bordas
        T[0,i] = -3
        T[i,0] = -3
    
    for i in range(n+1):
        T[n, i] = 6 * (i/n) - 3
        T[i, n] = 6 * (i/n) - 3
     
    for i in range(1,n): # criando o centro da matriz com o valor inicial
        T[i, 1:n] = t0[(n-1)*(i-1) : (n-1)*(i-1) + n-1]
    
    return T


def iteração_SOR(w, n, t0):
    '''Esta função recebe ômega, o valor de n e o chute inicial
    e realiza uma iteração SOR'''
    T = matriz_temperatura(n, t0) # chamando a função que cria a matriz temperatura
    sol_aprox = []
    
    for i in range(1, n):
        for j in range(1, n):
            T[i,j] =(1-w) * T[i,j] + (w/4) * (T[i-1,j] + T[i, j-1] + T[i,j+1] + T[i+1, j]) # Iteração SOR utilizando a equação 1 dada pelo EP                                     
            sol_aprox.append(T[i,j])                                                       
    return sol_aprox

# Perceba que as iterações do SOR podem ser otimizadas pelo formato da matriz T, por isso que a criei

def erro_infi(v_a, v_b):
    '''Esta função recebe dois vetores e calcula o erro sobre a norma infinita dos mesmos'''
    v_a = np.array(v_a)             # Convertendo para array tipo numpy///
    v_b = np.array(v_b)
    v = np.abs(v_a - v_b)           # calculando o módulo do vetor diferença
    return max(v)


def método_SOR(w, t0 , n, tol , max_iter = 600):
    '''Esta função recebe como parâmetros: ômega, o chute inicial, o valor de n, a tolerância para as iterações e a qtd de iterações 
    máximas e retorna a quantidade de iterações que é preciso para atingir a tolerância e a solução aproximada'''
    sol_ant = t0
    no_pause = True                                                                 # indicador de passagem para sair do laço
    k = 1                                                                           # Para contar a qtd de iterações
    while no_pause and k<= max_iter:
        sol_aprox_k = iteração_SOR(w, n, sol_ant)                                   # iterando com ômega, n e o chute inicial        
        if erro_infi(sol_aprox_k, sol_ant) / erro_infi(sol_aprox_k, t0) < tol:      #critério de parada
            no_pause = False                                                        # indicando a saída do laço
        sol_ant = sol_aprox_k
        k +=1
    return k-1 , sol_aprox_k                                                        # Perceba que também retorna a solução aproximada



def comp_omega(n, t0):
    '''Esta função recebe o valor de "n" e o valor inicial e compara os valores de ômega a serem implementados no método SOR 
    como é solicitado pelo EP com uma tolerância de convergência de 0.001, retornando uma lista com a qtd de iterações em cada ômega'''
    i = 0
    lista_iter = []
    while i <= 100:
        qtd_iter = método_SOR(1 + i/100, t0 , n, tol = 0.001)[0] # Armazenando a quantidade de iterações necessárias
        lista_iter.append(qtd_iter)
        i += 1
    return lista_iter

def elemento_minimo(lista):
    '''Esta função recebe um array e retorna a posição do elemento mínimo deste array e o elemento mínimo'''
    for i in range(len(lista)):
        if lista[i] == min(lista):
            return i, lista[i]



# Esta parte do código é para analisar os casos de comparção do ômega com chute inicial nulo.

#t0 = np.zeros((511**2))                  # Determinando o chute inicial nulo de dimensão (n-1)^2
#ou
t0 = []                                   # Determinando o chute inicial aleatório de dimensão (n-1)^2
for i in range(511**2):
    t0.append(random.random())

lista_iterações = comp_omega(512, t0)    # Gerando uma lista de iterações com o valor de n e o chute inicial (comp_omega(n, t0)) para cada ômega entre (1,2)
print(lista_iterações)                   # Imprime a lista de iterações
print(elemento_minimo(lista_iterações))  # Imprime a posição que possui "i" do ômega que gerou a menor qtd de iterações e a esta qtd de iterações
                                         # Para determinar ômega basta fazer 1 + i/100


# Esta parte do código é para plotar um gráfico comparando os valores de ômega com a qtd de iterações
lista_omegas = []                       # Gerando uma lista com os valores de ômega
for i in range(101):
    lista_omegas.append(1 + i/100)

plt.plot(lista_omegas, lista_iterações) # Plotando o gráfico com a lista de ômegas e qtd de iterações necessárias para atingir a tolerância


plt.title('Para n = 512, chute inicial aleatório, tol = 0.001') # Legendas do gráfico 
plt.xlabel('valores de omega')
plt.ylabel('qtd de iterações')

plt.show()