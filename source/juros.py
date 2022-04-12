from black import get_gitignore


valorD = float(input("escreva o valor de depósito: "))
taxa = float(input("escreva a taxa de juros: "))
valorM = float(input("diga quanto deseja depositar ao mês: "))

juros = valorD * taxa * 24
soma = (valorM * taxa * 24) + juros

print(f"o valor depositado depois dos 24 meses foi de R${soma:.2f} e foi depositado R${valorM:.2f} ao mes depois do primeiro depósito com uma taxa de juros ao mes de {taxa:.0f}%.")
wewewwewewe
