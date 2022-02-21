ganho = float(input('quanto ganha por hora?'))
h_trabalhadas = int(input('Horas trabalhadas por mês: '))

salario_bruto = ganho * h_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

print(f'valor tomado:{ir + inss + sindicato}')
print(f'salario Liquido:{salario_bruto - (ir + inss + sindicato)}')