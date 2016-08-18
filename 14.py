def collatz(n):
    seq=[]
    while n > 1:
        if n%2==0:
            n=n/2
            seq.append(n)
        elif n%2==1:
            n=(3*n)+1
            seq.append(n)
    seq.append(1)
    return len(seq)

bigest=0
for k,i in enumerate(range(0,1000000)):
    tam = collatz(i)
    if tam > bigest:
        bigest=tam
        index=k

print(index)
