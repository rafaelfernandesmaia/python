# EXERCICIO 01
'''contador = 0
while contador <= 10:
    print(contador)
    contador += 1'''

# EXERCICIO 02
'''soma = 0
contador = 0
while contador < 5:
    num = int(input('Digite um valor: '))
    soma += num
    contador += 1
print(f'A soma total dos 5 números foi {soma}')'''

# EXERCICIO 03
'''numsecret = 7
palpites = int(input('Digite um palpite: '))
while palpites != numsecret:
    if palpites < numsecret:
        print('Tente um valor mais alto')
    else:
        print('Tente um valor mais baixo')
    palpites = int(input('Digite um palpite: '))
print('Parabéns. Você acertou!!')'''

# EXERCICIO 04
'''cont = 0
num = int(input('Digite um valor: '))
print('==' * 11)
while cont <= 10:
    total = num * cont
    print(f'{num} x {cont} = {total}')
    cont += 1
print('==' * 11)'''

# EXERCICIO 05
'''num = int(input('Digite um valor: '))
while num != 0:
    if num != 0:
        if num % 2 == 0:
            print('Esse número é PAR')
        else:
            print('Esse número é IMPAR')
    num = int(input('Digite um valor: '))'''

# EXERCICIO 06
'''num = int(input('Digite um valor para fatorial: '))
fatorial = 1
contador = 1
while fatorial <= num:
    fatorial *= contador
    contador += 1
print(f'O fatorial de {num} é {fatorial}')'''

