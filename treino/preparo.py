# EXERCÍCIO 01
'''
print("Olá, Mundo!")
'''

# EXERCÍCIO 02
''' 
nome = str(input("Qual é o seu nome? "))
print(f'Muito prazer em te conhecer {nome}!')
'''

# EXERCÍCIO 03
'''
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print(f'A soma entre {n1} e {n2} é igual a {s}')
'''

# EXERCÍCIO 04
'''
frase = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(frase))
print('Só tem espaços?', frase.isspace())
print('É um número?', frase.isnumeric)
print('É alfabético?', frase.isalpha)
print('É alfanúmerico?', frase.isalnum)
print('Está em maiúsculas', frase.isupper)
print('Está em minúsculas', frase.islower)
print('Está capitalizada?', frase.istitle)
'''

# EXERCÍCIO 05
'''
num = int(input('Digite um número: '))
print(f'Analisando o número {num}, seu antecessor é {num-1} e o seu sucessor é {num+1}')
'''

# EXERCÍCIO 06
'''
num = int(input('Digite um número: '))
print(f'O dobro de {num} vale {num*2}\nO triplo de {num} vale {num*3}\nA raiz quadrada de {num} é igual a {num**(1/2):.2f}')
'''

# EXERCÍCIO 07
'''
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print(f'A média entre {n1} e {n2} é igual a {m:.1f}')
'''

# EXERCÍCIO 08
'''
d = float(input('Uma distância em metros: '))
print(f'A medida de {d}m corresponde a\n{d/1000}km\n{d/100}hm\n{d/10}dam\n{d*10:.0f}dm\n{d*100:.0f}cm\n{d*1000:.0f}mm')
'''

# EXERCÍCIO 09
'''
num = int(input('Digite um número para ver sua tabuada: '))
print('--' * 12)
for c in range(1, 11):
    print(f'{num} x {c} = {num*c}')
print('--' * 12)
'''

# EXERCÍCIO 10
'''
din = float(input('Quanto dinheiro você tem na carteira? R$ '))
dol = din / 4.96
print(f'Com R${din} você pode comprar US${dol:.2f}')
'''

# EXERCÍCIO 11
'''
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².')
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')
'''