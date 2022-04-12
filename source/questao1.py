valor = 0#INICIO DO PROGRAMA
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0
while (True):#ENTREOU NO LAÇO DE REPETIÇÃO
    valor = input() # VALOR DAS CÉDULAS]
    if valor == "":
        valor == str(valor)
        break
    valor = int(valor)
    print(f'Trocando {valor} por: ')
    n100 = valor // 100
    valor = valor - n100*100
    if n100 > 0:#ENTROU NAS CONDIÇÕES PARA VALIDAR SE VAI OU NÃO SER NECESSÁRIO FAZER A TROCA DE VALORES
        plural = "s" if n100 >= 2 else ""
        print(2 * " " ,f'{n100} nota{plural} de 100 reais')#SAÍDA DO PROGRAMA
    n50 = valor // 50
    valor = valor - n50*50
    if n50 > 0:
        plural = "s" if n50 >= 2 else ""
        print(2 * " " ,f'{n50} nota{plural}  de 50 reais')#SAÍDA DO PROGRAMA
    n20 = valor // 20
    valor = valor - n20* 20
    if n20 > 0:
        plural = "s" if n20 >= 2 else ""
        print(2 * " " ,f'{n20} nota{plural} de 20 reais')#SAÍDA DO PROGRAMA
    n10 = valor // 10
    valor = valor - n10*10
    if n10 > 0:
        plural = "s" if n10 >= 2 else ""
        print(2 * " " ,f'{n10} nota{plural} de 10 reais')#SAÍDA DO PROGRAMA
    n5 = valor // 5
    valor = valor - n5*5
    if n5 > 0:
        plural = "s" if n5 >= 2 else ""
        print(2 * " " ,f'{n5} nota{plural} de 5 reais')#SAÍDA DO PROGRAMA
    n2 = valor // 2
    valor = valor - n2*2
    if n2 > 0:
        plural = "s" if n2 >= 2 else ""
        print(2 * " " ,f'{n2} nota{plural} de 2 reais')#SAÍDA DO PROGRAMA
    n1 = valor // 1
    valor = valor - n1*1
    if n1 > 0:
        plural = "s" if n1 >= 2 else ""
        print(2 * " " ,f'{n1} moeda{plural} de 1 real')#SAÍDA DO PROGRAMA

