def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

x=0
while x < 100000:
    num = str(fib(x))
    if len(num) == 1000:
        index=x
        x = 1000001
    x+=1

print (num)
print(index)
