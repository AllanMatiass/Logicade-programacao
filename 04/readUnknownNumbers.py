# Escrever um algoritmo que leia uma quantidade desconhecida de
# números e conte quantos deles estão nos seguintes intervalos:
# [0.25], [26,50], [51,75] e [76,100]. A entrada de dados deve
# terminar quando for lido um número negativo.

n = float(input('Digite um numero: '))
t1 = 0
t2 = 0
t3 = 0
t4 = 0


while n >= 0:
    if n in range(0, 26):
        print('Grupo 1')
        t1 += 1

    elif n in range(26, 51):
        print('Grupo 2')
        t2 += 1

    elif n in range(51, 76):
        print('Grupo 3')
        t3 += 1

    elif n in range(76, 101):
        print('Grupo 4')
        t4 += 1
    else:
        print('Não está nos ranges;')
    
    n = float(input('Digite um numero: '))

print(f'Numeros digitados no G1: {t1}')
print(f'Numeros digitados no G2: {t2}')
print(f'Numeros digitados no G3: {t3}')
print(f'Numeros digitados no G4: {t4}')