fat = int(input('fat: '))

result = 1

for i in range(2, fat + 1):
  result *= i
  print(i)
print(result)
