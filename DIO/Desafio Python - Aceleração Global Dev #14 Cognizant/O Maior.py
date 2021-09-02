# Desafio
# Desenvolva um programa capaz de ler três valores e apresentar o maior deles e adicionar a mensagem “ eh o maior”. Use a seguinte forma como base:

# MaiorAB = (a+b+abs(a-b))/2

# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido pela mensagem " eh o maior".


import math
a, b ,c= map(eval, input().split())

maior2 = max(a, b, c);

print("%i eh o maior" %maior2)