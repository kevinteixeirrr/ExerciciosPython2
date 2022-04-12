from time import sleep

tb = int(input("tabuada de : "))
ini = int(input("inicio da tabuada: "))
fim = int(input("fim da tabuada: "))
while ini <= fim:
    sleep(0.4)
    print( f"{tb} +"+f" {ini} = ", tb + ini)
    ini += 1




