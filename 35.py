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

def isCircularPrime(n):
    lista = str(n)
    rotacao = []
    for k, v in enumerate(lista):
        tamanho = len(lista)
        rot=lista[k + 1:] + lista[:k + 1]
        rotacao.append(rot)
        num = [str(x) for x in rotacao]
        num1 = ''.join(num)
        if not isPrime(num1):
            return False
        rotacao = []
    return True

x = range(0, 1000000)
primes = []
for i in x:
    if isPrime(i):
        primes.append(i)
circPrimes = []
for prime in primes:
    if isCircularPrime(prime):
        circPrimes.append(prime)
print(circPrimes)
resultado = len(circPrimes)
print("Resposta: " + str(resultado))
