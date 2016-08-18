def factorial(n):
    fact=1
    while n > 1:
        fact=fact*n
        n-=1
    return fact

fac=factorial(100)
num = str(fac)
soma = 0
for i in num:
    soma+=int(i)
print(soma)
