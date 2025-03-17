# Elabore um programa que leia um número e imprima todos os
# números divisíveis por 4 que sejam menores que este número lido

n = int(input('Digite um numero: '))

for i in range(n):
    if i % 4 == 0 and i != 0:
        print(i)