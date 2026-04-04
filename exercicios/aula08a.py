from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Tente adivinhar qual é esse número?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais alto. Tente novamente')
        elif jogador > computador:
            print('Mais baixo. Tente novamente')
print(f'Você acertou com {palpites} palpites. Parábens!')