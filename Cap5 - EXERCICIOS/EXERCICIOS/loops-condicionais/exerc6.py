# Exercício 6 - Crie uma variável chamada contador = 0. 
# Enquanto counter for menor que 100, imprima os valores na tela,mas quando for encontrado o valor 23, 
# interrompa a execução do programa

print('CONTANDO ATÉ 23'.center(60))
print('-' * 60)
print('')


contador = 0

for i in range(100):
    print(i)
    contador += 1
    if i == 23:
        break