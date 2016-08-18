def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def isTruncatableLeft(n):
    lista = str(n)
    tamanho = len(lista)
    listaNova = []
    a = 0
    for k, i in enumerate(lista):
        tamanho = len(lista) - k
        listaNova.append(lista[0:tamanho])
        num = [str(x) for x in listaNova]
        num1 = ''.join(num)
        if not isPrime(num1):
            return False
        listaNova = []
    return True

def isTruncatableRight(n):
    lista = str(n)
    tamanho = len(lista)
    listaNova = []
    a = 0
    for k, i in enumerate(lista):
        tamanho = len(lista)
        listaNova.append(lista[k:tamanho])
        num = [str(x) for x in listaNova]
        num1 = ''.join(num)
        if not isPrime(num1):
            return False
        listaNova = []
    return True

x = range(0, 1000000)
primes = []
for i in x:
    if isPrime(i):
        primes.append(i)
truncPrimes = []
for prime in primes:
    if isTruncatableRight(prime) and isTruncatableLeft(prime):
        truncPrimes.append(prime)
print(truncPrimes)
print(len(truncPrimes))
soma = 0
for num in truncPrimes:
    soma = soma + num
resultado = soma - 17
print("Resposta: " + str(resultado))

# Tentativa inicial
# def isTruncatableRight (n):
#     lista=str(n)
#     tamanho=len(lista)
#     listaNova=[]
#     a=0
#     while a<=tamanho-1:
#         for i in lista[a:tamanho-1]:
#             listaNova.append(i)
#             print(listaNova)
#         num=[str(x) for x in lista]
#         num1=''.join(num)
#         print(num1)
#         if isPrime(int(num1)):
#             pass
#         else:
#             return False
#         listaNova=[]
#         a+=1
#     return True
