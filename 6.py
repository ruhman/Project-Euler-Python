def diference(num):
    sumSquare = 0
    squareSum = 0
    x= 1
    y= 1
    while x <= num:
        sumSquare = sumSquare + (x**2)
        print("X:",x)
        print("SumSquare:",sumSquare)
        x+=1
    while y <= num:
        squareSum = squareSum + y
        print("Y:",y)
        print("SquareSum:",squareSum)
        y+=1
    squareSum = squareSum ** 2
    return sumSquare - squareSum

dif = diference(100)
print("Result:", dif)
