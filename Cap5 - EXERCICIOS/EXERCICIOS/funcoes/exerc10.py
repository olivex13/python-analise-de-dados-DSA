# Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10

print('NUMEROS MENORES QUE 5'.center(60))
print('-' * 60)
print('')

menores5 = [ x for x in range(10) if x < 5]

print(menores5)