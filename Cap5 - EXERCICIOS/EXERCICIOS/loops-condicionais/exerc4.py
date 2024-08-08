# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

print('SEQUENCIA DE NUMEROS PARES ENTRE 100 E 150'.center(60))
print('-' * 60)
print('')

pares = []

for i in range(100, 151):
    if i % 2 == 0:
        pares.append(i)

print(pares)


