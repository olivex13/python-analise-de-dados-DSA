# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. 
# Se o dia for igual a Domingo ou  igual a sábado, imprima na tela "Hoje é dia de descanso"
# caso contrário imprima na tela "Você precisa trabalhar!"

print('DIAS DA SEMANA'.center(60))
print('-' * 60)
print('')

diasDaSemana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']

diaAtual = input('Digite o dia da semana: ').lower()

while diaAtual not in diasDaSemana:
    print("Digite um dia da semana válido.")
    diaAtual = input('Digite o dia da semana: ').lower()

if diaAtual == 'sabado' or diaAtual == 'domingo':
    print('Hoje é dia de descando.')
else:
    print('Você precisa trabalhar!')