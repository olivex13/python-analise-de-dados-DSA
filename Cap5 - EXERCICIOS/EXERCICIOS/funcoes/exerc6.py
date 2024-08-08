# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
"""total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)"""

total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)

# A variável global TOTAL está atribuido o valor de 0 
# A váriavel local TOTAL está retornando o resultado da função SOMA

  