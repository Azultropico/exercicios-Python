sexo = int(input('digite 1 para homem ou 2 para moça:'))
h = float(input('digite sua altura: '))

if sexo == 1:
    vm = (72.7 * h) - 58
    print('seu peso ideal é',vm)

elif sexo == 2:
    vf = (62.1 * h) - 44.7
    print('seu peso ideal é',vf)