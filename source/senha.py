#em construção
#subprograma
def md(valor1, valor2):
    while True:
        if valor1 != valor2:
            print("senha invalida")
            valor2 = int(input())
        else:
            print("senha correta")
            break
#a
#programa principal
senha1 = 2002
senha2 = int(input())
md(senha1,senha2)