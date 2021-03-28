kg_allowed_in_SP = 50
fine_per_kg = 4
value_of_fine = 0

kg_fish = float(input('kg pescado: '))

if kg_fish > kg_allowed_in_SP:
  value_of_fine += fine_per_kg * (kg_fish - kg_allowed_in_SP) 

print('valor da multa: ', value_of_fine)