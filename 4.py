i=100
j=100
palindromes =[]
for i in range(100,1000):
    for j in range(100,1000):
        mult = i * j
        la = list(str(mult))
        if la == list(reversed(la)):
            s = ''.join(map(str, la))
            palindromes.append(int(s))
print(max(palindromes))
