qtdTestes = int(input())
qtdValoresTestes = int(input())#quantidade de valores teste
valormi = float(input())#valor maximo e abaixo valor minimo
valormax = float(input())

for i in range(qtdTestes):# n vezes para rodar o progragrama

    abaixo = 0
    soma = 0
    acima = 0
    intervalo = 0

    for j in range(qtdValoresTestes):#1 a 6

        valores = 0
        valores = float(input())#valores de 1 ate 6 do for

        if valores < valormi:
            valores = 0
            abaixo = abaixo + valores + 1

        if valores > valormax:
            valores = 0
            acima = acima + valores + 1

        if valores >=valormi and valores <= valormax: #soma dos intervalos
            intervalo += 1
            soma += valores

    if soma > 5:#sida para o usuário
        print(f"Teste 1: ")
    else:
        print(f"Teste 2: ")

    print(2 * " ", "Intervalo: [{}, {}]".format(valormi, valormax))
    print(2 * " ", "Abaixo do Intervalo: {}, No Intervalo: {},\nAcima do Intervalo: {}.".format(abaixo, intervalo, acima))
    if soma > 5:
        print(2 * " ", "Soma dos Valores Dentro do intervalo: {}".format(soma))
    else:
        print(2 * " ","Soma de Valores no Intervalo: {}".format(soma))