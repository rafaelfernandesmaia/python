'''
# Função
def calcular_area(larg, comp):
    area = larg * comp
    print(f"A área de um terreno de {larg} x {comp} é de {area}m²")


# Programa principal
print("Controle de terrenos")
print("--" * 13)
larg = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))
calcular_area(larg, comp)
'''

# Função
'''
def contagem_regressiva(numero):
    for i in range(numero, 0 ,-1):
        print(i)

contagem_regressiva(10)
'''

# Função
def escreva(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)


# Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')