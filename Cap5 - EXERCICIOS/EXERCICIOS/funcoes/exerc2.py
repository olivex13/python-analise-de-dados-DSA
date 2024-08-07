# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

print('STRING EM LETRA MAIÚSCULA'.center(60))
print('-' * 60)   
print('')

string = input("Digite sua frase aqui: ")

def stringMaiuscula(string):
    maiuscula = string.upper()
    return maiuscula

maiuscula = stringMaiuscula(string)

print('')
print(maiuscula)