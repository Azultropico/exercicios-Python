salario = float(input('digite seu salário:'))

print(f'soldo inicial:{salario}')

if 280>= salario:
    ns = salario * 0.2
    print(f'valor do aumento:{ns}')

elif salario >=700 and salario <=1500:
    ns = salario * 0.10
    print(f'valor do aumento:{ns}')
elif salario >=280 and salario <=700:
    ns = salario * 0.15
    print(f'valor do aumento:{ns}')
elif salario <= 1500:
    ns = salario * 0.05
    print(f'valor do aumento:{ns}')

print(f'soldo após o aumento{salario + ns}')



