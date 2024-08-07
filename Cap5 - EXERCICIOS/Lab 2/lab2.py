print('CALCULADORA PYTHON'.center(60))
print('-' * 60)
print('')

def soma(num1, num2):
    total = num1 + num2
    return(f'RESULTADO: {num1} + {num2} = {total}')

def subtracao(num1, num2):
    total = num1 - num2
    return(f'RESULTADO: {num1} - {num2} = {total}')

def multiplicacao(num1, num2):
    total = num1 * num2
    return(f'RESULTADO: {num1} * {num2} = {total}')

def divisao(num1, num2):
    total = num1 / num2
    return(f'RESULTADO: {num1} / {num2} = {total}')

print('Selecione a opção desejada: \n')
print(' 1 - SOMA \n 2 - SUBTRAÇÃO \n 3 - MULTIPLICAÇÃO \n 4 - DIVISÃO \n')
print('')

while True:
    opcao = int(input('Digite sua opção: (1, 2, 3, 4): '))
    if opcao in [1, 2, 3, 4]:
        break
    else:
        print('Digite uma opção válida.')

print('')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
print('')
if opcao == 1:
    resultado = soma(num1, num2)
    
elif opcao == 2:
    resultado = subtracao(num1, num2)
    
elif opcao == 3:
    resultado = multiplicacao(num1, num2)
    
elif opcao == 4:
    resultado = divisao(num1, num2)
    
print(resultado)

