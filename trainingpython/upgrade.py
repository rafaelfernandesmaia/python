# Python - Curso em Video Exercícios

# 001
'''
print("Olá, Mundo!")
print("Me livrei da maldição")
'''

# 002
'''
name = input("Qual é o seu nome: ")
print(f"É um prazer te conhecer {name}")
'''

# 003
'''
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
print(f"A soma entre {n1} e {n2} é igual a {s}")
'''

# 004
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

# 005
'''
num = int(input("Digite um número: "))
print(f"Analisando o valor {num}, seu antecessor é {num-1} e seu sucessor {num+1}")
'''

# 006
'''
num = int(input("Digite um número: "))
print(f"O dobro de {num} vale {num*2}\nO triplo de {num} vale {num*3}\nA raiz quadrada de {num} é igual a {num**(1/2):.2f}")
'''

# 007
'''
n1 = float(input("Primeira Nota do aluno: "))
n2 = float(input("Segunda Nota do aluno: "))
m = (n1 + n2) / 2
print(f"A média entre {n1} e {n2} é {m:.1f}")
'''

# 008
'''
dist = float(input("Uma distância em metros: "))
print(f"A medida de {dist}m corresponde a\n{dist/1000}km\n{dist/100}hm\n{dist/10}dam\n{dist*10}dm\n{dist*100}cm\n{dist*1000}mm")
'''

# 009
'''
num = int(input('Digite um número para ver sua tabuada: '))
print('------------')
print(f"{num} x 1 = {num*1}")
print(f"{num} x 2 = {num*2}")
print(f"{num} x 3 = {num*3}")
print(f"{num} x 4 = {num*4}")
print(f"{num} x 5 = {num*5}")
print(f"{num} x 6 = {num*6}")
print(f"{num} x 7 = {num*7}")
print(f"{num} x 8 = {num*8}")
print(f"{num} x 9 = {num*9}")
print(f"{num} x 10 = {num*10}")
print('------------')
'''

# 010
'''
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.15
print(f"Com R${real} você pode comprar US${dolar:.2f}")
'''

# 011
'''
lar = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = lar * alt
print(f"Sua parede tem a dimensão de {lar}x{alt} e sua área é de {area}m2")
print(f"Para pintar essa parede, você precisará de {area/
'''

# 012
'''
produto = float(input("Qual é o valor do produto: R$ "))
print(f"O produto que custava R${produto}, na promoção com desconto de 5% vai custar R${produto*0.95:.2f}")
'''

# 013
'''
func = float(input("Qual é o salário do funcionário? R$ "))
print(f"Um funcionário que ganhava R${func}, com 15% de aumento, passa a receber R${func*1.15:.2f}")
'''

# 014
'''
cel = float(input("Qual é a temperatura em °C: "))
print(f'A temperatura convertida em {cel*1.8+32}°F')
'''

# 015
'''
dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
total = (dias * 60) + (km * 0.15)
print(f"O total a pagar é R${total:.2f}")
'''

# 016
'''
import math
num = float(input("Digite um valor: "))
print(f"O valor digitado foi {num} e sua porção inteira é {math.trunc(num)}")
'''

# 017
'''
import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hip = math.hypot(co, ca)
print(f"A hipotenusa vai medir {hip:.2f}")
'''

# 018
'''
import math
ang = int(input("Digite o ângulo que você deseja: "))
sen = math.sin(math.radians(ang))
print(f"O ângulo de {ang} tem o SENO de {sen:.2f}")
cos = math.cos(math.radians(ang))
print(f"O ângulo de {ang} tem o COSSENO de {cos:.2f}")
tan = math.tan(math.radians(ang))
print(f"O ângulo de {ang} tem o TANGENTE de {tan:.2f}")
'''

# 019
'''
import random
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f"O aluno escolhido foi {escolhido}")
'''

# 020
'''
import random
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("A ordem da apresentação será ")
print(lista)
'''

# 021
# Tocando MP3

# 022
'''
nome = str(input("Digite seu nome: "))
print("Analisando seu nome")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome ao todo tem {len(nome) - nome.count(" ")}")
prime = nome.split()
print(f"Seu primeiro nome é {prime[0]} e ele tem {len(prime[0])}")
'''

# 023
'''
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
'''

# 024
'''
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
'''

# 025
'''
nome=str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
'''

# 026
'''
f=str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {f.count('A')} vezes na frase.')
print(f'A primeira letra A apareceu na posição {f.find('A')+1}')
print(f'A última letra A apareceu na posição {f.rfind('A')+1}')
'''


# 027
'''
n=str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')
'''

# 028