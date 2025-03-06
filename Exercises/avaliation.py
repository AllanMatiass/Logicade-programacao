avaliation = float(input('Digite uma nota: '))

while (avaliation < 0) or (avaliation > 10):
    avaliation = float(input('Digite uma nota: '))

print(f'nota: {avaliation}')