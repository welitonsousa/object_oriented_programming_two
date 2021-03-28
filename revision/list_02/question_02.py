price_alcool = 3.45
price_gasolina = 4.53

fuel_type = input('G-gasolina\nA-alcool\ntipo do combustivel: ')
fuel_volume = float(input('volume em litros: '))

pay_value = 0

if fuel_type == 'G':
  discount = 0
  if fuel_volume > 20:
    discount = 0.06
  else:
    discount = 0.04

  pay_value = price_gasolina * fuel_volume * discount

else:
  discount = 0
  if fuel_volume > 20:
    discount = 0.05
  else:
    discount = 0.03

  pay_value = price_alcool * fuel_volume * discount

print(pay_value)

