x = 0
s = 0
m = 0
while True :
    intt = input(": ")
    if intt != "":
        intt = int(intt)
        x = x + intt
        s = s + 1
        m = x / s
    if intt == "":
        intt = str(intt)
        break
print(x,s,m)

