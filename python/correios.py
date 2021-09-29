#exercicio 1
# x = float(input('digite o numero da alegria: '))
# print(f'O número informado foi:{x}')

#exercicio 2
# y = float(input('digite o primeiro numero: '))
# z = float(input('digite o segundo numero: '))

# j = y + z

# print(j)

#exercicio 3
# sexo = int(input('digite 1 para homem ou 2 para moça:'))
# h = float(input('digite sua altura: '))

# if sexo == 1:
#     vm = (72.7 * h) - 58
#     print('seu peso ideal é',vm)

# elif sexo == 2:
#     vf = (62.1 * h) - 44.7
#     print('seu peso ideal é',vf)

#exercicio 4
# ganho = float(input('quanto ganha por hora?'))
# h_trabalhadas = int(input('Horas trabalhadas por mês: '))

# salario_bruto = ganho * h_trabalhadas
# ir = salario_bruto * 0.11
# inss = salario_bruto * 0.08
# sindicato = salario_bruto * 0.05

# print(f'valor tomado:{ir + inss + sindicato}')
# print(f'salario Liquido:{salario_bruto - (ir + inss + sindicato)}')

#exercicio 5
# letra = (input('digiter "f" para feminino ou "m" para masculino: '))

# if letra == 'f':
#     print('sexo Meminino')
# elif letra == 'm':
#     print('sexo Masculino')
# else:
#     print('sexo invalido')

#exercicio 6
# nota1 = int(input('digite a primeira nota: '))
# nota2 = int(input('digite a segunda nota: '))

# media = (nota1 + nota2) / 2

# if 10> media >= 7:
#     print('aprovado')
# elif media < 7:
#     print('reprovado')
# elif media == 10:
#     print('aprovado com distinção')

#exercicio 7
# ganho = float(input('quanto ganha por hora? '))
# h_trabalhadas = int(input('Horas trabalhadas por mês: '))

# bruto = ganho * h_trabalhadas

# sindicato = 0.03 *bruto
# cinco = 0.05 *bruto
# dez = 0.1 *bruto
# fgts = 0.11 *bruto
# vinte = 0.2 *bruto

# if bruto<= 900:
#     print(f'salario bruto R$:{bruto}')
#     print(f'valor roubado R$:{sindicato}')
#     print(f'FGTS R$:{fgts}')
#     print(f'salario líquido R${bruto-sindicato}')
# elif bruto <= 1500:
#     print(f'salario bruto R$:{bruto}')
#     print(f'valor roubado R$:{sindicato}')
#     print(f'FGTS R$:{fgts}')
#     print(f'salario líquido R${bruto-sindicato - cinco}')
# elif bruto <= 2500:
#     print(f'salario bruto R$:{bruto}')
#     print(f'valor roubado R$:{sindicato}')
#     print(f'FGTS R$:{fgts}')
#     print(f'salario líquido R${bruto-sindicato -dez}')
# elif bruto > 2500:
#     print(f'salario bruto R$:{bruto}')
#     print(f'valor roubado R$:{sindicato}')
#     print(f'FGTS R$:{fgts}')
#     print(f'salario líquido R${bruto-sindicato - vinte}')


#exercicio 8
# alt_inicial = float(input('qual a altura da arvore? '))
# taxa = float(input('qual o taxa de crescimento ao ano? '))
# ano = int(input('qual a quantidade de anos? '))

# x = (ano * taxa  / 100) + alt_inicial


# print(f'Altura final: {x}metros.)

# valor_base = float(input('digite o valor base: '))

# jan = valor_base
# fev = (jan * 0.05) + valor_base
# mar = (fev * 0.05) + valor_base
# abr = (mar * 0.05) + valor_base
# mai = (abr * 0.05) + valor_base
# jun = (mai * 0.05) + valor_base
# jul = (jun * 0.05) + valor_base
# ago = (jul * 0.05) + valor_base
# sete = (ago * 0.05) + valor_base
# out = (sete * 0.05) + valor_base
# nov = (out * 0.05) + valor_base
# dez = (nov * 0.05) + valor_base

# print(f'anuidade:R${jan + fev + mar + abr + mai + jun + jul + ago + sete + out + nov + dez}.')





