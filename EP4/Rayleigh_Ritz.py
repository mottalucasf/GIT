# ---------------------------------------------
# Exercício de Programação 4  - MAP5729 2020
#
# O método de Rayleigh_Ritz 
# 
# Lucas Motta Freire
# ---------------------------------------------

import numpy as np
import algoritmo_thomas as thm  # Módulo para utilizar o algoritmo de Thomas na resolução so sistema



#---------------------------------------------------------------------
# Funções auxiliares para o cálculo do minimizador global do funcional
#---------------------------------------------------------------------


# Construindo os vetores da matriz tridiagonal simétrica A do sistema normal
def vectors_A(a, b, lamb, n):
    '''Parâmetros:
        a, b = extremos do intervalo; lamb = valor de lâmbda;  n = dimensão do problema
        
    Retorna: O vetor diagaonal inferior e o vetor diagonal da matriz do sistema normal, nesta ordem'''
    
    diag = np.zeros(n)
    sub_diag = np.zeros(n-1)
    
    for i in range(n):
        diag[i] = 2 * ((n+1)/(b-a)) + ((2 * lamb)/3) * ((b-a)/(n+1)) # decorrente do produto interno L
    for i in range(n-1):
        sub_diag[i] = -((n+1)/(b-a)) + lamb/6 * ((b-a)/(n+1))        # decorrente do produto interno L

    return sub_diag, diag

# Calculando o vetor minimizador
def vector_minimizador(a, b, lamb, n, vec_d):
    '''Parâmetros:
        a, b = extremos do intervalo; lamb = valor de lâmbda;  
        n = dimensão do problema; vec_d = vetor independente do sistema
    
    Retorna: Solução do sistema normal(vetor minimizador) utilizando o algoritmo de Thomas'''

    vec_a = vectors_A(a, b, lamb, n)[0]
    vec_b = vectors_A(a, b, lamb, n)[1]
    vec_c = vectors_A(a, b, lamb, n)[0]

    c = thm.solução_sistema(vec_a, vec_b, vec_c, vec_d)

    return c

#-------------------------------------------
# Funções auxiliares para a análise do erro
#-------------------------------------------

# Erro - norma infinita
def erro_infi(v_a, v_b):
    ''' Esta função recebe dois vetores e calcula o erro sobre a norma infinita dos mesmos'''
    v_a = np.array(v_a)             # Convertendo para array tipo numpy///
    v_b = np.array(v_b)
    v = np.abs(v_a - v_b)           # calculando o módulo do vetor diferença
    return max(v)


#----------------------------------------------------------
# Funções auxiliares para a implementando da função u_barra
#----------------------------------------------------------

# Construindo as funções chapéu
def phi(i, y, a, b, n):
    '''Parametros
    i = índice da função chapéu; y = o valor a ser calculado pela i-ésima função chapéu
    a = extremo inferior do intervalo a definir as funções chapéu; b = extremo superior do intervalo a definir as funções chapéu
    n = determina a qtd de pontos da partição
    
    Retorna: O valor da i-ésima função chapéu calculada em y '''
    
    h = (b-a) / (n+1)
    x = np.linspace(a, b, n+2)                        # Gerando nós
    
    if  x[i-1] <= y <= x[i]:
        return (y - x[i-1])/h
    
    elif x[i] <= y <= x[i+1]:
        return (x[i+1] - y)/h

    else:
        return 0
 
def phi_vector(y, a, b, n):
    '''Esta função cria um vetor de dimensão "n" cuja a i-ésima entrada é dada pelo valor da i-ésima função chapéu em y'''
    phi_x = np.zeros(n)
    for i in range(n):
        phi_x[i] = phi(i+1, y, a, b, n)
    return phi_x

