value = int(input('Taboada de: '))
start = int(input('comecar em: '))
end = int(input('terminar em: '))

for index in range(start, end + 1):
  print(value, ' x ', index, ' = ', value * index)