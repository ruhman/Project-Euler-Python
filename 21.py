def checkDivs(n):
    lista=[]
    for i in range (1,n//2):
        if n%i==0:
            lista.append(i)
    return lista

def sumDivs(list):
    soma=0
    for num in list:
        soma+=num
    return soma

amicable=[]
for i in range (1,1000):
    divs=checkDivs(i)
    soma=sumDivs(divs)
    divsSoma=checkDivs(soma)
    somaDiv=sumDivs(divsSoma)
    if soma == somaDiv:
        if soma != somaDiv:
            amicable.append(soma)
            amicable.append(somaDiv)
        else:
            amicable.append(soma)
print(amicable)
resp = sumDivs(amicable)
print(resp)
