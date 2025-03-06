# While true proibido


menor = float(input('Digite o numero: '))
counter = 0

while counter < 100:
    c = float(input('Digite o numero: '))
    if c < menor:
        menor = c
    
    counter += 1

print(menor)