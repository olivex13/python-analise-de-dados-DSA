# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

print('ADCIONANDO ITENS A LISTA'.center(60))
print('-' * 60)   
print('')

lista = ['Homem de Ferro', 'Capitão america', 'Hulk', 'Thor']

def adcionarLista (lista):
    item1 = input("Qual Herói deseja adcionar a lista? ")
    lista.append(item1)
    item2 = input("Qual o outro Herói deseja adcionar a lista? ")
    lista.append(item2)
    return lista

listaAtualizada = adcionarLista(lista)

print(listaAtualizada)