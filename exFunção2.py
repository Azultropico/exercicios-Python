num = float(input('digite seu argumento: '))

def negativo_positivo(num):
    if num<=0:
        return 'negativo'
    elif num>0:
        return 'positivo'
result = negativo_positivo(num)
print(result)