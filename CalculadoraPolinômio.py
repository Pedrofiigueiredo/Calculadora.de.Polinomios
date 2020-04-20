'''Criei duas funções além das especificadas (RecebePolinomio() e opcoes()) para não repetir o mesmo procedimento várias vezes.'''

# Receber o polinômio
def RecebePolinomio():
    grau = int(input('Digite o grau do polinômio: '))
    print()
    polinomio = [0]*(grau+1)
    indice = [0]*(grau+1)

    # Cria um vetor com o índice decrescente do polinômio. Exemplo [3, 2, 1, 0]
    for expoente in range(grau, -1, -1):
        indice[grau-expoente] = expoente

    # Recebe os termos digitados pelo usuário e de acordo com o expoente
    for termo in range(grau,-1,-1):
        polinomio[grau-termo] = int(input('Digite o termo x{}: '.format(termo)))
    
    return polinomio

# Escolher outra função do programa usando o menu
def opcoes():
    # Depois de selecionar uma opção, o usuáiro pode selecionar outra sem reiniciar
    opc = input('Deseja fazer alguma outra operação? (s/n): ')

    while opc != 's' and opc != 'n':
        opc = input('Deseja fazer alguma outra operação? (s/n): ')
    if opc == 's':
        main()
    if opc == 'n':
        print('''\nPedro Figueiredo Dias - 41990455\n''')


# Mostar o polinômio formatado
def MostraPolinomio(polinomio):
    grau = len(polinomio) - 1
    indice = [0]*(grau+1)

    for expoente in range(grau+1, -1, -1):
        indice[grau - expoente] = expoente

    for e in range(grau+1):
        # Termo x^1 (para não mostrar o expoente)
        if indice[e] == 1 and polinomio[e] > 0:
            print('+{0}x '.format(polinomio[e]), end='')
        elif indice[e] == 1 and polinomio[e] < 0:
            print('{0}x '.format(polinomio[e]), end='')

        # Termo independente
        elif indice[e] == 0 and polinomio[e] > 0:
            print('+{0}'.format(polinomio[e]))
        elif indice[e] == 0 and polinomio[e] < 0:
            print('{0}'.format(polinomio[e]))

        # Os demais termos
        elif polinomio[e] > 0:
            print('+{0}x^{1} '.format(polinomio[e], indice[e]), end='')
        elif polinomio[e] < 0:
            print('{0}x^{1} '.format(polinomio[e], indice[e]), end='')

# Calcular valor do polinômio
def valorPolinomio(polinomio, X):
    grau = len(polinomio) - 1
    indice = [0]*(grau+1)
    soma = 0

    for expoente in range(grau+1, -1, -1):
        indice[grau - expoente] = expoente

    for e in range(grau+1):
        # Termo independente (soma sem expoente nenhum)
        if indice[e] == 0:
            soma += polinomio[e]
        # Demais termos
        else:    
            x = X ** indice[e]
            soma += polinomio[e] * x
    
    return soma

# Calcular a soma dos polinômios
def somaPolinomio(p1, p2):
    # Se os polinômios tiverem o mesmo grau
    if len(p1) == len(p2):
        p_somados = [0]*len(p2)

        for p in range(len(p1)):
            p_somados[p]  = p1[p] + p2[p]
    
    # Se os graus forem diferentes
    else:
        # Verifica qual é o polinômio de maior grau
        if len(p1) > len(p2):
            maior = p1
            menor = p2
            dif = len(p1) - len(p2)
        else:
            maior = p2
            menor = p1
            dif = len(p2) - len(p1)
        
        # Define o tamanho do vetor resultado
        p_somados = [0]*len(maior)

        # Adiciona os termos de diferença entre os polinômios no vetor resultado, já que não há como somá-los (expoentes que não tem nos dois polinômios)
        for e in range(dif):
            p_somados[e] = maior[e]

        # Soma os termos restantes (só com expoentes iguais) e adiciona no vetor resultado. 
        for r in range(len(menor)):
            p_somados[r+1] = menor[r] + maior[r+1]

    return p_somados
    
# Calcular a multiplicação dos polinômios
def multiplicaPolinomio(p1, p2):
    grau_p1 = len(p1) - 1
    grau_p2 = len(p2) - 1
    p_multiplicado = [0]*(grau_p1 + grau_p2 + 1)

    # Multiplicação distributiva de cada termo do primeiro polinômio com cada termo do segundo polinômio.
    for p in range(len(p1)):  
        for q in range(len(p2)):
            # Deixa os resultados com o mesmo expoente juntos.
            p_multiplicado[p + q] += p1[p] * p2[q]
        
    return p_multiplicado

# Função principal
def main():
    # Menu usuário
    menu = int(input('''
    -- CALCULADORA DE POLINÔMIOS --

    O que você deseja fazer?

    [1] Calcular o VALOR de um polinômio
    [2] Calcular a SOMA de dois polinômios
    [3] Calcular a MULTIPLICAÇÃO de dois polinômios

    Sua opção: '''))

    # Valor do polinômio
    if menu == 1:
        print('\n--- Primeiro, defina o polinômio ---\n')
        polinomio = RecebePolinomio() # Recebe o polinômio usando a função
        print('\nSeu polinômio é:\nP(X) = ', end='')
        MostraPolinomio(polinomio)
        X = int(input('\nDigite o valor de X para o polinômio: '))
        print('\nP({0}) = {1}\n'.format(X, valorPolinomio(polinomio, X)))

        # Escolher outra opção do programa
        opcoes()

    # Soma        
    if menu == 2:
        print('\n--- Digite o PRIMEIRO polinômio, P(X) ---\n')
        p1 = RecebePolinomio()
        print('\n--- Digite o SEGUNDO polinômio, Q(X) ---\n')
        p2 = RecebePolinomio()
        print('\nOs polinômios são:\nP(X) = ', end='')
        MostraPolinomio(p1)
        print('Q(X) = ', end='')
        MostraPolinomio(p2)
        print()

        # Calcula e imprime o resultado da soma
        resultado = somaPolinomio(p1, p2)
        print('P(X) + Q(X) = ', end='')
        MostraPolinomio(resultado)
        print()

        # Escolher outra opção
        opcoes()

    # Multiplicação
    if menu == 3:
        print('\n--- Digite o PRIMEIRO polinômio, P(X) ---\n')
        p1 = RecebePolinomio()
        print('\n--- Digite o SEGUNDO polinômio, Q(X) ---\n')
        p2 = RecebePolinomio()
        print('\nOs polinômios são:\nP(X) = ', end='')
        MostraPolinomio(p1)
        print('Q(X) = ', end='')
        MostraPolinomio(p2)
        print()

        # Calcula e imprime o resultado da multiplicação
        resultado = multiplicaPolinomio(p1, p2)
        print('P(X) * Q(X) = ', end='')
        MostraPolinomio(resultado)
        print()

        # Escolher outra opção
        opcoes()

main()