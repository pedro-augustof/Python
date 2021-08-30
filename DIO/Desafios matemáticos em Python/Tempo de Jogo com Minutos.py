# Desafio
# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

i, im, f, fm = map(int, input().split())

if f>i and fm>=im:
    h = f - i
    m = fm - im
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif f>i and im>fm:
    h = (f - i) - 1
    m = (60 - im) + fm
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif i>f and fm>=im:
    h = (24 - i) + f
    m = fm - im
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif i>f and im>fm:
    h = ((24 - i) + f) - 1
    m = (60 - im) + fm
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif i==f and im>=fm:
    h = 23
    m = (60 - im) + fm
    if m == 60:
        h = 24
        m = 0
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h, m))
elif f==i and fm>=im:
    m = fm - im
    print("O JOGO DUROU 0 HORA(S) E %i MINUTO(S)" %(m))
elif i==f and im==fm:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
'''
a, b, c, d = input().split(" ")
hora_inicial = int(a)
minuto_inicial = int(b)
hora_final = int(c)
minuto_final = int(d)

if (hora_inicial > hora_final):
    hora = int((24 - hora_inicial) + hora_final)
elif (hora_inicial < hora_final):
    hora = int(hora_final - hora_inicial)
else:
    if (minuto_final <= minuto_inicial):
        hora = int(24)
    else:
        hora = int(0)

if (minuto_final > minuto_inicial):
    minuto = int(minuto_final - minuto_inicial)
elif (minuto_final < minuto_inicial):
    minuto = int((60 - minuto_inicial) + minuto_final)
    hora = hora - 1
else:
    minuto = int(0)

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minuto))
'''