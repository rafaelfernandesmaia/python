import random

def palpite():
    print('Pensei em um número! Você consegue adivinhar...')
    while True:
        chute = int(input('Digite um número entre 1 a 10: '))

        if chute > sorteio:
            print('Menos... Tente novamente!')
        elif chute == sorteio:
            print('Parábens! Você acertou')
            break
        else:
            print('Mais... Tente novamente!')

jogando = True

while jogando:
    sorteio = random.randint(1, 10)
    print('-' * 25)
    print('JOGO DA ADIVINHAÇÃO'.center(25))
    print('-' * 25)
    palpite()

    resposta = input('Quer jogar de novo? (S/N): ').strip().upper()
    if resposta != 'S':
        jogando = False

print('Obrigado por jogar!')