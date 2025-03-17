# Escreva um que solicita 10 números ao usuário, e ao final mostre
# os dois maiores números digitados pelo usuário.
counter = 0
bigger1 = 0
bigger2 = 0


while counter <= 10:
    n = int(input('Digite o numero: '))

    if n > bigger1:
        print('Aq1')
        bigger2 = bigger1
        bigger1 = n

    elif n > bigger2:
        print('Aq2')
        bigger2 = n
    
    counter += 1

print(f'Maiores: {bigger1} e {bigger2}')