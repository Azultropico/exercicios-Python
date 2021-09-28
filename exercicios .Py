#exercicio 1
 x = float(input('digite o numero da alegria: '))
 print(f'O número informado foi:{x}')

#exercicio 2
 y = float(input('digite o primeiro numero: '))
 z = float(input('digite o segundo numero: '))

 j = y + z

 print(j)

#exercicio 3
 sexo = int(input('digite 1 para homem ou 2 para moça:'))
 h = float(input('digite sua altura: '))

 if sexo == 1:
     vm = (72.7 * h) - 58
     print('seu peso ideal é',vm)

 elif sexo == 2:
     vf = (62.1 * h) - 44.7
     print('seu peso ideal é',vf)

#exercicio 4
 ganho = float(input('quanto ganha por hora?'))
 h_trabalhadas = int(input('Horas trabalhadas por mês: '))

 salario_bruto = ganho * h_trabalhadas
 ir = salario_bruto * 0.11
 inss = salario_bruto * 0.08
 sindicato = salario_bruto * 0.05

 print(f'valor tomado:{ir + inss + sindicato}')
 print(f'salario Liquido:{salario_bruto - (ir + inss + sindicato)}')
