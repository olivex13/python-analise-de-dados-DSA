# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. 
# Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

print('NUMEROS PARES ENTRE 4 E 20'.center(60))
print('-' * 60)
print('')


lista = []
variavel = 4

while variavel <= 20:
    if variavel % 2 == 0:
        lista.append(variavel)
    variavel += 1

print(lista)

