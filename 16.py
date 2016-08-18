n = 2**1000
numero=list(str(n))
emOrdem = sorted(numero)
sums=[]
for i in range (1,10):
    num = str(i)
    r= emOrdem.count(num)
    mult = r*i
    sums.append(mult)
total=0
for i in sums:
    total = total + i
print(total)
