'''def validacao(valor):
    if valor == 11:
        print("São paulo")
    elif valor == 21:
        print("Rio de janeiro")
    elif valor == 61:
        print("Brasília")
    elif valor == 71:
        print("salvador")



#programa principal
ddd = int(input())
validacao(ddd)'''

'''for i in range(0, 101, 2 ):
    print(i)'''

'''for i in range(6):
    valores =float(input())
    media = valores /6.0
    
    for i in range(valores):
        print(i, media)'''

'''a = float(input())


b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
s=0
m =0
t =[a,b,c,d,e,f]
for n in t:
  if n > 0:
    s = s + 1
    m = m + (n)
print('{} valores positivos'.format(s))
print('{:.1f}'.format(m/s))'''


def verifica(valores):
    dentro = 0
    fora = 0
    for i in range(valores):
        x = int(input())
        if x >= 10 and x <= 20:
            dentro = dentro + 1
        else:
            fora = fora + 1
    print('{} in'.format(dentro))
    print('{} out'.format(fora))


n = int(input())
verifica(n)
