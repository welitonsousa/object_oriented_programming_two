impost_renda = 0.11
impost_inss = 0.08
impost_sindicato = 0.05

salary = float(input('salrio bruto: '))

"""calculate value of imposts"""
pay_renda = salary - (salary * impost_renda)
pay_inss = salary - (salary * impost_inss)
pay_sindicato = salary - (salary * impost_sindicato)

pay_total = pay_renda + pay_inss + pay_sindicato

print('salario bruto: ', salary)
print('INSS: ', pay_inss)
print('Sindicato: ', pay_sindicato)
print('saalrio liquido: ', salary - pay_total)