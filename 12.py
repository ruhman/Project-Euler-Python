def genTriangleNumbers(limit):
    nums=[]
    last=0
    i=0
    while (last <= limit):
        last=last+i
        nums.append(last)
        i+=1
    return nums

def checkNumDivisors(n):
    count=1 # accounts for 'n' and '1'
    i=2
    while(i**2 < n):
        if(n%i==0):
            count+=2
        i+=1
    count+=(1 if i**2==n else 0)
    return count

triangleNums=genTriangleNumbers(100000000000)
for k,i in enumerate(triangleNums):
    divs = checkNumDivisors(i)
    print(str(i) + ": " + str(divs)+ " index: "+str(k))
    if divs >= 500:
        print(str(i)+" é a resposta!!!")
        break
