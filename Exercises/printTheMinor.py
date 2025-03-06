def printb(txt):
    print('-' * 50)
    print(txt)
    print('-' * 50)

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('DIgite o terceiro numero: '))


if n1 == n2 and n1 == n3:
    printb('iguais')
else:
    if n1 < n2:
        menor = n1
    else:
        menor = n2
    
    if n3 < menor:
        menor = n3

print(menor)
