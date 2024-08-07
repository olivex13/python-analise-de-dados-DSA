# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números      

print('IMPRIMINDO NUMEROS PARES'.center(60))
print('-' * 60)   
print('')

lista = []

for i in range(21):
    lista.append(i)

def numerosPares(lista):
    numerosPares = []
    for i in lista:
        if i % 2 == 0:
            numerosPares.append(i)
    return numerosPares

pares = numerosPares(lista)

print(pares)