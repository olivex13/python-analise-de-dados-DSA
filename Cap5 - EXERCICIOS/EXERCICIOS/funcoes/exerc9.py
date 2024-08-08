# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]

print('PALAVRAS COM "A" NO NOME '.center(60))
print('-' * 60)
print('')

palavrasComA = [x for x in palavras if 'a' in x]

print(palavrasComA)