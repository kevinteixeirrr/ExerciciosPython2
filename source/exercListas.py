# subprograma
def funcao(el, nTV, xiz):
    while xiz < nTV:
        if xiz == nTV:
            break
        el.append(int(input()))
        xiz += 1
        men = l[0]
        maxi = l[0]
        for i in range(len(el)):
            el.sort()
            if maxi < el[i]:
                maxi = el[i]
            elif men > el[i]:
                men = el[i]

    print(f"o menor é o n: {men} o maior é o n: {maxi} a quantifdade de n acumulados é de {xiz} e a lista na qual foram estraidpos os dados é a {el}")


# programa principal
l = []
x = 0
n = int(input("escreva o numero total de vezes:"))
funcao(l, n, x)
