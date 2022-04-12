def seletorCar(valores):
    # 1 maneir de se fazer
    for andei in valores:
        print(f"eu andei no {andei} ")
        return andei


# tuplas
carros = ("fiat", "chevrolet", "toyota")
seletorCar(carros)

# 1 maneir de se fazer
for andei in carros:
    print (f"eu andei no {andei}")

#3 maneira de se fazer
for pos, andei in enumerate(carros):
    print(f"eu andei no {andei} N: {pos}")

#3 maneira de se fazer
for cont in range(0, len(carros)):
    print(cont, carros[cont])

print(sorted(carros))

a = (1, 2, 3, 4, 5, 6)
b = (4, 2, 1, 5, 8)
c = a + b
print(c.count(2))
print(c.index(2))
