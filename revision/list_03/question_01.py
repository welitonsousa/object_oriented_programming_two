base = int(input('base: '))
expoente = int(input('expoente: '))

result = 1
for i in range(0, expoente):
  result *= base
print(result)
