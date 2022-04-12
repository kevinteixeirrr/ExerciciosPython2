notas = [10 , 5 , 7 , 9, 6]
soma = 0
x = 0 
s = 0
while x < 5:
    soma += notas[x]
    x += 1
s = soma/x
print(f"media: {s}")