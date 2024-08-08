# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. 
# Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada com 4 elementos

print('ARGUMENTO FORMAL'.center(60))
print('-' * 60)
print('')

lista = [1, 5, 10, 15]

def multiplicar (numero, lista):
    resultado = [numero * i for i in lista]
    return resultado

resultado1 = multiplicar(2, [1])
resultado2 = multiplicar(2, lista)
    
print(resultado1)
print(resultado2)    

