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

# EXERCÍCIO 12
'''
preco = float(input('Qual é o preço do produto? R$ '))
preal = preco * 0.95
print(f'O produto que custava {preco}, na promoção com desconto de 5% vai custar {preal:.2f}')
'''

# EXERCÍCIO 13
'''
sal = float(input('Qual é o salário do Funcionário? R$ '))
preal = sal * 1.15
print(f'Um funcionário que ganhava R${sal}, com 15% de aumento, passa a receber R${preal:.2f}')
'''

# EXERCÍCIO 14
'''
c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32
print(f'A temperatura de {c}°C corresponde a {f}°F!')
'''

# EXERCÍCIO 15
'''
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
diasal = dias * 60
kmrod = 0.15 * km
tot = diasal + kmrod
print(f'O total a pagar é de R${tot}')
'''

# EXERCÍCIO 16
'''
from math import trunc
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e sua porção inteira é {trunc(num)}')
'''

# EXERCÍCIO 17
'''
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.sqrt(co**2 + ca**2)
print(f'A hipotenusa vai medir {h:.2f}')
'''

# EXERCÍCIO 18
'''
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')
'''

# EXERCÍCIO 19
'''
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
'''

# EXERCÍCIO 20
'''
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem da apresentação será ')
print(lista)
'''

# EXERCÍCIO 21
#FEITO - MÚSICA

# EXERCÍCIO 22
'''
nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {(nome.upper())}')
print(f'Seu nome em minúsculas é {(nome.lower())}')
print(f'Seu nome ao todo {(len(nome) - nome.count(' '))} letras')
print(f'Seu primeiro nome tem {(nome.find(' '))} letras')
'''

# EXERCÍCIO 23
'''
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dentena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
'''

# EXERCÍCIO 28
from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! EU pensei no número {computador} e não no {jogador}')