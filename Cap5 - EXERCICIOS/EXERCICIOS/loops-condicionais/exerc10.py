# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 

print('CONTANDO A LETRA R'.center(60))
print('-' * 60)
print('')


frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 

contagem = frase.lower().count('r')
print(frase)
print('A letra R aparece {} vezes na frase'.format(contagem))