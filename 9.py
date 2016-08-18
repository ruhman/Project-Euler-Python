for a in range (0,1001):
  for b in range (0,1001):
      for c in range (0,1001):
          if a**2+b**2==c**2:
              if a<b and b<c:
                  if a+b+c == 1000:
                      mult = a*b*c
                      print(mult)
