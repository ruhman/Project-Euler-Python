
def findPrime(until):
    x = list(range(1,until))
    for i in x:
        for j in x:
            if j != i:
                if j % i == 0:
                    x.remove(j)
    return x

until = 10
while True:
    primes = findPrime(until)
    if (len(primes)>=10000):
        print("Resposta:",primes[10000])
        print("Tamanho",len(primes))
        print("Lista:",primes)
        break
    else:
        until = until * 5
    print("Quantidade de primos:",len(primes))
