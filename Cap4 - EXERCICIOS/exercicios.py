print("Exercicios DSA - PYTHON PARA ANALISE DE DADOS E DATA SCIENCE".center(60))
print('-'*60)

# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

print('EXERCICIO 1:')
exerc1 = list(range(1, 11))
print(exerc1)
print('')

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
print('EXERCICIO 2:')
exerc2 = [17, "Zaya", [18, 2, 33], "Homem de Ferro", 3.14]
print(exerc2)
print('')

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
print('EXERCICIO 3:')
str1 = "Homem"
str2 = " de Ferro"
str3 = str1 + str2
print(str3)
print('')

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função 
# count do objeto tupla para verificar quantas vezes o número 4 aparece na tupla

print('EXERCICIO 4:')
exerc4 = (1, 2, 2, 3, 4, 4, 4, 5)
quantidade = exerc4.count(4)
print(quantidade)
print('')

# Exercício 5 - Crie um dicionário vazio e imprima na tela
print('EXERCICIO 5:')
exerc5 = {}
print(exerc5)
print('')

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
print('EXERCICIO 6:')
exerc6 = {'Fernando': 150, 'André': 300, 'Luiz': 450}
print(exerc6)
print('')

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
print('EXERCICIO 7:')
exerc6['João'] = 600
print(exerc6)
print('')

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
print('EXERCICIO 8:')
exerc8 = {'Tony Stark': 100, 'Hulk': 200, 'Thanos': [100, 200]}
print(exerc8)
print('')

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.
print('EXERCICIO 9:')
exerc9 = ['Vingadores', (10, 20), {'Capitão America': 100, 'Homem de Ferro': 200}, 3.14]
print(exerc9)
print('')

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
print('EXERCICIO 10:')
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[1:18])

