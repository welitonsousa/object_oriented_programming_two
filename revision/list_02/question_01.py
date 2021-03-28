def verify_type_triangle(sides: list) -> str:
  count_sides = count_values(sides)
  if count_sides == 3:
    return 'equilatero'
  elif count_sides == 2:
    return 'isoceles'
  return 'escaleno'

def count_values(sides: list) -> int:
  repetition_return = 0
  for index in sides:
    repetition = 0
    for element in sides:
      if index == element:
        repetition += 1
    if repetition > repetition_return:
      repetition_return = repetition
  return repetition_return   

sides = [int(input('lado 01: ')), int(input('lado 02: ')), int(input('lado 03: '))]

big_value = max(sides)
sides.remove(big_value)

if big_value < sides[0] + sides[1]:
  sides.append(big_value)
  print(verify_type_triangle(sides))
else:
  print('nao eh um triangulo')

