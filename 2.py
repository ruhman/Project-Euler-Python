def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)
sum=0
for index, fibonacci_number in enumerate(fib()):
     print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
     if fibonacci_number % 2 ==0:
         sum = sum+fibonacci_number
     if index == 33:
         break
print(sum)
