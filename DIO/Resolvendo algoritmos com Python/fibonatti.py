# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 46).

# Saída
# Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.

n = int(input())
fib_list = [0]
n = n - 1
a = 0
b = 1
for i in range(n):
    som = a + b
    a = b
    b = som
    fib_list.append(a)


print(fib_list)
fib_string = (' '.join(str(x) for x in fib_list))
print(fib_string)
