# WHILE - EXERCICIOS

# Contagem simples
'''contador = 0
while contador <= 10:
    print(contador)
    contador += 1'''

# Contagem regressiva
'''contador = 10
while contador >= 0:
    print(contador)
    contador -= 1'''

# Somando números
'''soma = 0
contador = 1
while contador <= 5:
    num = int(input('Digite um valor: '))
    soma += num
    contador += 1
print(f'A soma entre os 5 números será {soma}')'''

# Tabuada
'''contador = 1
num = int(input('Digite um valor: '))
while contador <= 10:
    total = num * contador
    print(f'{num} x {contador} = {total}')
    contador += 1
print('==' * 11)'''

# FOR - EXERCICIOS

# Contagem simples
'''for n in range(1, 11):
    print(n)'''

# Contagem regressiva
'''for n in range(10, 0, -1):
    print(n)'''

# Números Pares
'''for num in range(0, 21):
    if num % 2 == 0:
        print(num, end=' ')'''

# Tabuada
'''num = int(input('Digite um valor: '))
for contador in range(1, 11):
    total = num * contador
    print(f'{num} x {contador} = {total}')'''

# Soma de Valores
'''soma = 0
for c in range(1, 101):
    soma += c
print(f'A soma é {soma}')'''

# Contar letras
'''palavra = str(input('Digite uma palavra: '))
contador = 0
for letra in palavra:
    contador += 1
print(f'A palavra tem {contador} letras')'''