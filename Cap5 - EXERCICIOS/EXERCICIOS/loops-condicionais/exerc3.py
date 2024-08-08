# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

print('MULTIPLICANDO ELEMENTOS DA TUPLA'.center(60))
print('-' * 60)
print('')

tupla = (4, 6, 8, 10)

resultado = []

for i in tupla:
    total = i * 2
    resultado.append(total)

print(resultado)