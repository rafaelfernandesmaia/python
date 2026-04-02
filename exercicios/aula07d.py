print('-=-' * 11)
print('BEM VINDO A TABUADA')
print('-=-' * 11)
num = int(input('Digite um número: '))
for c in range(0, 11):
    m = num * c
    print(f'{num} x {c} = {m}')