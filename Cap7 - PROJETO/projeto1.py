import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _= system ('cls')
    else:
        _= system('clear')

def game():
    limpa_tela()
    print('\n Bem vindo(a) ao jogo da forca!')
    print('Advinhe a palavra a baixo:\n')

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    letras_erradas = []

    while chances > 0:
        print(' '.join(letras_descobertas))
        print(f'Chances restantes: {chances}')
        print('Letras erradas:', ' '.join(letras_erradas))

        tentativa = input('Digite uma letra: ').lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas(index) = letra
                index += 1
        else: 
            chances -= 1
            letras_erradas.append(tentativa)


    

