# Desafios
# Crie um programa que leia um número e mostre os números pares até esse número, inclusive ele mesmo.

# Entrada
# Você receberá 1 valor inteiro N, onde N > 0.

# Saída
# Exiba todos os números pares até o valor de entrada, sendo um em cada linha. 

n = int(input())
for i in range(n+1):
  if (i%2) == 0:
    if i != 0: 
      print(i)