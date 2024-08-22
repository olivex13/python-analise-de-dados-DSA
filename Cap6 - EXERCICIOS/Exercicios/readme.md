
# EXERCICIOS - PYTHON DATA SCIENCE ACADEMY 💣

Exercicios referente ao Capitulo 6

- Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

- Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
```python
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)
```

- Exercício 3 - Calcule a matriz transposta da matriz abaixo.
 Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
```python
matrix = [[1, 2],[3,4],[5,6],[7,8]]
```
- Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
Aplique as duas funções aos elementos da lista abaixo. 
Obs: as duas funções devem ser aplicadas simultaneamente.
```python
lista = [0, 1, 2, 3, 4]
```
- Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado ao elemento correspondente na listaB.
```python
listaA = [2, 3, 4]
listaB = [10, 11, 12]
listaA = [2, 3, 4]
listaB = [10, 11, 12]
```
- Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
```python
range(-5, 5)
```
- Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
```python
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
```
- Exercício 8 - Considere os dois dicionários abaixo. 
Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
```python
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}
```
- Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
```python
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```
- Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras Data e Science na frase: 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'
```python
import re
texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'
```
