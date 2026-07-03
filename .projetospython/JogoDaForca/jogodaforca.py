# Planejamento do projeto

# 1 O programa escolhe uma palavra aleatória de uma lista
# 2 Mostra a palavra "escondida" com underlines (_ _ _ _ _)
# 3 O jogador digita uma letra por vez
# 4 Se a letra existe na palavra, ela é revelada nas posições certas
# 5 Se não existe, o jogador perde uma tentativa
# 6 O jogo acaba quando: o jogador acerta a palavra toda ou as tentativas acabam

import random

palavras = ['python', 'programação', 'computador', 'algoritmo', 'forca']
palavra_secreta = random.choice(palavras)

letras_descobertas = ['_'] * len(palavra_secreta)

erros = []

max_erros = 6

print('Bem-vindo ao Jogo da Forca')
print('Adivinhe a palavra secreta')
print(' '.join(letras_descobertas))

while True:
    letra = str(input('\nDigite uma letra: ')).lower()

    if letra in letras_descobertas or letra in erros:
        print('Você já tentou essa letra')
        continue

    if letra in palavra_secreta:
        print(f'Boa! A letra {letra} está na palavra')
        for i, char in enumerate(palavra_secreta):
            if char == letra:
                letras_descobertas[i] = letra
    
    else:
        print(f'A letra {letra} NÃO ESTÁ NA PALAVRA')
        erros.append(letra)

    print('Palavra:', ' '.join(letras_descobertas))
    print('Erros:', ', '.join(erros))
    print(f'Tentativas restantes: {max_erros - len(erros)}')

    if '_' not in letras_descobertas:
        print('Parábens, você venceu! A palavra era ', palavra_secreta)
        break

    if len(erros) >= max_erros:
        print('\nGAME OVER! Você perdeu')
        print(f'A palavra era {palavra_secreta}')
        break