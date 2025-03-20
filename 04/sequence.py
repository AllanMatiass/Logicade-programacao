#Dada a sequência matemática de números 2, 3, 5,8,13, 21....
#Construa um programa que calcule a soma desta sequência
#para os N primeiros termo onde, N é fornecido pelo usuário.
#• Exemplo: N=5 S= 2+3+5+8+13 =31


term = int(input('Digite o numero de termo: '))

counter = 0
s = 0

while counter < term:
    n = int(input('Digite um numero: '))
    s += n
    counter += 1


print(s)