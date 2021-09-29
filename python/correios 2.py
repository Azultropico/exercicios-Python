#exercicio 5
# letra = (input('digiter "f" para feminino ou "m" para masculino: '))

# if letra == 'f':
#     print('sexo Meminino')
# elif letra == 'm':
#     print('sexo Masculino')
# else:
#     print('sexo invalido')

#exercicio 6
nota1 = int(input('digite a primeira nota: '))
nota2 = int(input('digite a segunda nota: '))

media = (nota1 + nota2) / 2

if 10> media >= 7:
    print('aprovado')
elif media < 7:
    print('reprovado')
elif media == 10:
    print('aprovado com distinção')
