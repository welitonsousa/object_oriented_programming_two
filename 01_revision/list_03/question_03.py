
while (True):
  fat = int(input('fat: '))
  if fat == 0: 
    break
  if fat < 17:
    result = 1
    for i in range(2, fat + 1):
      result *= i
      print(i)
    print(result)
