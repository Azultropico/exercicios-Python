def valorPagamento(a,b):
    multa = (a + 3/100)
    juros = (a + 0.1/100) * b
    valorfinal = a + multa + juros

    if b == 0:
        return a
    
    elif b > 0:
        return valorfinal

lista1 = []
lista2 = []

while True:

    vparcela = float(input('Digite o valor da parcela: \n'))
    if vparcela == 0:
         break
    dias = int(input('Digite a quantidade de dias de atraso: \n'))

    result = valorPagamento(vparcela, dias)
    lista1.append(result)
    lista2.append(dias)

print(f'valor da parcela {lista1}')
print(f'quantidade de dias de atraso{lista2}')


#atividade nova

num = float(input('digite seu argumento: '))

def funcao(num):
    if num<=0
        return 'negativo'
    elif num>0
        return 'positivo'
result = funcao(num)
print(result)
