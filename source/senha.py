while True:
    senha1 = 2002
    senha = input()
    if senha != senha1:
        print("senha invalida")
        senha = input()
    if senha == "10001":
        print("senha correta")
        break
