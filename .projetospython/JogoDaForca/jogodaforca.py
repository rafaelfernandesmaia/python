# Planejamento do projeto

# 1 O programa escolhe uma palavra aleatória de uma lista
# 2 Mostra a palavra "escondida" com underlines (_ _ _ _ _)
# 3 O jogador digita uma letra por vez
# 4 Se a letra existe na palavra, ela é revelada nas posições certas
# 5 Se não existe, o jogador perde uma tentativa
# 6 O jogo acaba quando: o jogador acerta a palavra toda ou as tentativas acabam

import random

palavras = ["flamengo", "palmeiras", "corinthians", "gremio", "santos"]

palavra_secreta = random.choice(palavras)
letras_descobertas = ["_"] * len(palavra_secreta)
tentativas = 6
letras_usadas = []

while tentativas > 0:
    print(f"\nPalavra: {' '.join(letras_descobertas)}")
    print(f"Tentativas restantes: {tentativas}")
    
    chute = input("Digite uma letra: ").lower()

    # Verifica se a letra já foi usada antes
    if chute in letras_usadas:
        print("Você já tentou essa letra!")
        continue  # volta pro início do loop sem gastar tentativa

    letras_usadas.append(chute)

    if chute in palavra_secreta:
        print("Acertou!")
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == chute:
                letras_descobertas[i] = chute
    else:
        print("Errou!")
        tentativas -= 1

    # Verifica se o jogador já descobriu a palavra toda
    if "_" not in letras_descobertas:
        print(f"\nParabéns! Você acertou a palavra: {palavra_secreta}")
        break
else:
    print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")