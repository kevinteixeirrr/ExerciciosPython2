# subprograma
def calcular(valor1, valor2, valor3):
    r = 0
    if valor2 == "+":
        r = valor1 + valor3
    elif valor2 == "-":
        r = valor1 - valor3
    elif valor2 == "*":
        r = valor1 * valor3
    elif valor2 == "/":
        r = valor1 / valor3
    elif valor2 == "**":
        r = valor1 ** valor3
    else:
        valor2 = None
        r = None
        print(f"voce não escolheu nenhum {valor2} e o resultado foi {r}")
    print(f"voce escolheu {valor2} e o resultado foi {r}")


# programa principal
a = float(input("digite um numero: "))
op = input("qual operação deseja realizar ? (+) (-) (*)(/) ou (**)")
b = float(input("digite outro numero: "))
calcular(a, op, b)

'''n = int(input())
x = 1

while x <= 10:
    print(n+x)
    x += 1
'''
