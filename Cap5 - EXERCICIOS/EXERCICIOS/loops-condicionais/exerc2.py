# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

print('IDENTIFICANDO FRUTAS'.center(60))
print('-' * 60)
print('')

lista = ['Melancia', 'Uva', 'Banana', 'Morango']


print(f'LISTA DE FRUTAS: {lista}')

if 'Morango' in lista:
    print('Morango está na lista.')
else: 
    print('Morango não está na lista!')