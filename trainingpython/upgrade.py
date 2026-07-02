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
'''
import random
import time
computador = random.randint(0, 5)
print("-=-" * 18)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 18)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
time.sleep(0.5)
if jogador == computador:
    print("PARÁBENS, Você conseguiu me vencer!")
else:
    print(f"GANHEI!, Eu pensei no número {computador} e não no {jogador}")
'''

# 029
'''
velo = int(input("Qual é a velocidade do carro? "))
if velo <= 80:
    print("Tenha um bom dia, Dirija com segurança")
else:
    print("MULTADO!, Você excedeu o limite permitido que é de 80km/h")
    multa = (velo - 80) * 7
    print(f"Você deve pagar uma multa de R${multa:.2f}")
    print("Tenha um bom dia, Dirija com segurança")
'''

# 030
'''
num = int(input("Me diga um número: "))
if (num % 2 == 0):
    print(f"O número {num} é PAR")
else:
    print(f"O número {num} é IMPAR")
'''

# 031
'''
viagem = float(input("Qual é a distância de sua viagem? "))
print(f"Você está preste a começar uma viagem de {viagem:.1f}Km")
if (viagem <= 200):
    preco = viagem * 0.50
    print(f"E o preço de sua passagem será de R${preco:.2f}")
else:
    preco = viagem * 0.45
    print(f"E o preço de sua passagem será de R${preco:.2f}")
'''

# 032
'''
from datetime import date
bissexto = int(input("Que ano quer analisar? Coloque 0 como o ano atual: "))
if bissexto == 0:
    bissexto = date.today().year
if bissexto % 4 == 0 and (bissexto % 100 != 0 or bissexto % 400 == 0):
    print(f"O ano {bissexto} é BISSEXTO")
else:
    print(f"O ano {bissexto} não é BISSEXTO")
'''

# 033
'''
p1 = int(input("Primeiro valor: "))
p2 = int(input("Segundo valor: "))
p3 = int(input("Terceiro valor: "))
num = [p1, p2, p3]
print(f"O maior valor é {max(num)}")
print(f"O menor valor é {min(num)}")
'''

# 034
'''
salfunc = float(input("Qual é o salário do funcionário? R$ "))
if salfunc > 1250:
    novosal = salfunc * 1.10
    print(f"Quem ganhava R${salfunc:.2f} passa a ganhar R${novosal:.2f} agora")
else:
    novosal = salfunc * 1.15
    print(f"Quem ganhava R${salfunc:.2f} passa a ganhar R${novosal:.2f} agora")
'''

# 035
'''
print("-=-" * 15)
print("Analisador de triângulos")
print("-=-" * 15)
s1 = int(input("Primeiro segmento: "))
s2 = int(input("Segundo segmento: "))
s3 = int(input("Terceiro segmento: "))
if (s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s2 + s1):
    print("Os segmentos acima PODEM FORMAR um triângulo!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")
'''

# Capitulo 11 - Cores no terminal

# Mundo 2

# 036
'''
casa = float(input("Qual é o valor da casa? R$"))
sal = float(input("Qual é o salário do funcionário? R$"))
ano = int(input("Quantos anos de financiamento? "))
prestacao = casa / (ano * 12)
minimo = sal * 30 / 100
print(f"Para pagar uma casa de R${casa:.2f} em {ano} anos a prestação será de R${prestacao:.2f}")
if prestacao <= minimo:
    print("Empréstimo CONCEDIDO")
else:
    print("Empréstimo NEGADO")
'''

# 037
'''
num = int(input('Digite um número inteiro: '))
print('Escolha uma base de conversão: \n [1] converter para Binário \n [2] converter para Octal \n [3] converter para Hexadecimal')
opcao = int(input('Escolha a opção: '))
b = bin(num).replace('0b', '')
o = oct(num).replace('0o', '')
h = hex(num).replace('0x', '').upper()

if(opcao == 1):
    print('{} convertido para Binário é igual a: {}'.format(num, b))
elif(opcao == 2):
    print('{} convertido para Octal é igual a: {}'.format(num, o))
elif(opcao == 3):
    print('{} convertido para Hexadecimal é igual a: {}'.format(num, h))
else:
    print('Você não escolheu uma das opções.')
'''

# 038
'''
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
if n1 > n2:
    print("O PRIMEIRO valor é maior")
elif n1 < n2:
    print("O SEGUNDO valor é maior")
else:
    print("Os dois valores são IGUAIS")
'''

# 039
'''
from datetime import date
ano_nasc = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f"Quem nasceu em {ano_nasc} tem {idade} em {ano_atual}")
if idade < 18:
    alistar = 18 - idade
    print(f"Ainda faltam {alistar} anos para seu alistamento")
    print(f"Seu alistamento será em {ano_atual + alistar}")
elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE")
else:
    alistar = idade - 18
    print(f"Você já deveria ter se alistado há {alistar} anos")
    print(f"Seu alistamento foi em {ano_atual - alistar}")
'''

# 040
'''
n1 = float(input("Primeira Nota: "))
n2 = float(input("Segunda Nota: "))
media = (n1 + n2) / 2
print(f"Tirando {n1} e {n2}, a média do aluno é {media:.1f}")
if media >= 7:
    print("O aluno foi APROVADO")
elif 5 <= media <= 6.9:
    print("O aluno está de RECUPERAÇÃO")
else:
    print("O aluno foi REPROVADO")
'''

# 041
'''
from datetime import date
ano_nasc = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f"O atleta tem {idade} anos")
if idade <= 9:
    print("Classificação MIRIM")
elif idade <= 14:
    print("Classificação INFANTIL")
elif idade <= 19:
    print("Classificação JUNIOR")
elif idade <= 25:
    print("Classificação SENIOR")
else:
    print("Classificação MASTER")
'''

# 042
'''
ladoA = float(input("Primeiro lado: "))
ladoB = float(input("Segundo lado: "))
ladoC = float(input("Terceiro lado: "))
if (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB):
    if ladoA == ladoB and ladoB == ladoC and ladoA == ladoC:
        print("Os segmentos acima podem formar o triângulo EQUILÁTERO")
    elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
        print("Os segmentos acima podem formar o triângulo ESCALENO")
    else:
        print("Os segmentos acima podem formar o triângulo ISÓSCELES")
else:
    print("Os valores não podem formar um triângulo")
'''

# 043
'''
kg = float(input("Qual é o seu peso? (Kg) "))
alt = float(input("Qual é sua altura? (m) "))
imc = kg / alt ** 2
print(f"O IMC dessa pessoa é {imc:.1f}")
if imc < 18.5:
    print("Você está com ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("Você está com PESO IDEAL")
elif 25 <= imc < 30:
    print("Você está com SOBREPESO")
elif 30 <= imc < 40:
    print("Você está com OBESIDADE")
else:
    print("Você está com OBESIDADE MÓRBIDA")
'''

# 044
'''
print("========== LOJAS AMERICANAS ==========")
compra = int(input("Preço das compras: R$ "))
print("FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x cartão\n[ 4 ] 3x ou mais")
opcao = int(input("Qual é a sua opção? "))
if opcao == 1:
    money = compra * 0.90
    print(f"Seu produto que custava R${compra:.2f} vai passar a custar R${money:.2f}")
elif opcao == 2:
    money = compra * 0.95
    print(f"Seu produto que custava R${compra:.2f} vai passar a custar R${money:.2f}")
elif opcao == 3:
    print(f"Seu produto que custa R${compra:.2f} vai ser parcelado em 2x no cartão de R${compra/2:.2f}")
elif opcao == 4:
    money = compra * 1.20
    parcelas = int(input("Quantas parcelas? "))
    print(f"Sua compra será parcelada em {parcelas:.2f}x de R${money/parcelas:.2f} COM JUROS")
    print(f"Sua compra de R${compra:.2f} vai custar R${money:.2f} no final")
else:
    print("Opção INVÁLIDA. Tente novamente!")
'''

# 045
'''
import random
opcoes = ["pedra", "papel", "tesoura"]
escolha_pc = random.choice(opcoes)
escolha_Jogador = input("Escolha pedra, papel ou tesoura: ").lower()
print("==" * 14)
print(f"Computador escolheu: {escolha_pc}")
print(f"O Jogador escolheu: {escolha_Jogador}")
print("==" * 14)
if escolha_pc == escolha_Jogador:
    print
elif (escolha_Jogador == "papel" and escolha_pc == "pedra") or (escolha_Jogador == "tesoura" and escolha_pc == "papel") or (escolha_Jogador == "pedra" and escolha_pc == "papel"):
    print("Você VENCEU!!!")
else:
    print("O Computador VENCEU!!!")
'''

# 046
'''
import time
for c in range(10, -1, -1):
    print(c)
    time.sleep(0.5)
print("BUM! BUM! POOOW!")
'''

# 047
'''
for c in range(1, 50, 2):
    print(c+1, end=" ")
print("Acabou")
'''

# 048
'''
soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        cont += 1
print(f"A soma de todos os {cont} valores solicitados é {soma}")
'''

# 049
'''
num = int(input("Digite um número para ver sua tabuada? "))
for cont in range(1, 11):
    print(f"{num} x {cont} = {num*cont}")
'''

# 050
'''
soma = 0
par = 0
for cont in range(1, 7):
    num = int(input("Digite um número: "))
    cont += 1
    if num % 2 == 0:
        par += 1
        soma += num
print(f"A soma dos {par} números pares é {soma}")
'''

# 051
'''
print("===========================")
print("    10 TERMOS DE UMA PA    ")
print("===========================")
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print(c, end=" → ")
print("Acabou!")
'''

# 052
'''
num = int(input("Digite um número: "))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
print(f"O número {num} foi divido {cont} vezes")
if cont == 2:
    print("O número é PRIMO")
else:
    print("O número NÃO É PRIMO")
'''

# 053
'''
# Detector de Palíndromo

palavra = input("Digite uma palavra ou frase: ")

# Remove espaços e deixa tudo em minúsculo, para comparar corretamente
palavra_tratada = palavra.replace(" ", "").lower()

# Inverte a palavra usando slicing
palavra_invertida = palavra_tratada[::-1]

if palavra_tratada == palavra_invertida:
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo.')
'''

# 054
'''
from datetime import date
ano_atual = date.today().year
maiorI = 0
menorI = 0
for c in range(1, 8):
    ano_nasc = int(input(f"Em que ano a {c}. pessoa nasceu? "))
    if ano_atual - ano_nasc >= 18:
        maiorI += 1
    else:
        menorI += 1
print(f"Ao todo tivemos {maiorI} pessoas maiores de idade\nE também tivemos {menorI} pessoas menores de idade")
'''

# 055
'''
pesos = [float(input(f'Peso da {a}º pessoa: ')) for a in range(1, 6)]
print(f'O maior peso foi de {max(pesos)}Kg\nO menor foi de {min(pesos)}Kg!')
'''

# 056
'''
maiorI = 0
somaI = 0
maior_Idade = 0
mulherNova = 0
for cont in range(1, 5):
    print(f"----- {cont}ª PESSOA -----")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    somaI += idade
    if idade > maior_Idade:
        maior_Idade = idade
        mais_Velho = nome
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    if sexo in 'F' and idade < 20:
        mulherNova += 1
    cont += 1
print(f"A média do grupo é de {somaI/4:.1f} anos\nO homem mais velho do grupo tem {maior_Idade} e se chama {mais_Velho}\nAo todo são {mulherNova} mulheres com menos de 20 anos")
'''

# 057
'''
sexo = str(input("Informe seu sexo [M/F]: "))
while sexo != "M" and sexo != "F":
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).upper().strip()
if sexo == "M":
    print("Sexo M registrado com sucesso")
else:
    print("Sexo F registrado com sucesso")
'''

# 058
'''
from random import randint
numsorteado = randint(1, 10)
print('Tente adivinhar um número sorteado de 1 à 10...')
jogada = int(input('Qual o seu palpite: '))
cont = 1
while jogada != numsorteado:
    if jogada > numsorteado:
        print('Informe um valor menor...')
    elif jogada < numsorteado:
        print('Informe um valor maior...')
    jogada = int(input('Tente novamente: '))
    cont += 1
print(f'Parabéns, com {cont} tentativas você venceu!!!')
'''

# 059
'''
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
resposta = 0
while resposta != 5:
    print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
    resposta = int(input(">>>>> Qual é a sua opção? "))
    if resposta == 1:
        soma = n1 + n2
        print(f"A soma de {n1} e {n2} é igual a {soma}")
    elif resposta == 2:
        print(f"A multiplicação de {n1} e {n2} é igual a {n1*n2}")
    elif resposta == 3:
        if n1 == n2:
            print("Os valores são iguais")
        elif n1 > n2:
            print("O PRIMEIRO valor é MAIOR que o SEGUNDO")
        else:
            print("O SEGUNDO valor é MAIOR que o PRIMEIRO")
    elif resposta == 4:
        print("Informe os valores novamente...")
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
    elif resposta == 5:
        print("Finalizando...")
    else:
        print("Opção Inválida. Tente novamente.")
'''

# 060
'''
n1 = int(input('Digite um número para saber o fatorial: '))
f1 = 1
c1 = n1
while c1 > 1:
    f1 *= c1
    c1 -= 1
print(f'O resultado de {n1}! é  {f1}')
'''

# 061
'''
p = int(input('Qual o primeiro termo?  '))
r = int(input('E qual a razão?  '))
c = 1
while c <= 10:
    a = p + (c - 1) * r
    print(a, end='')
    print(' → ' if c < 10 else '. FIM! ', end='')
    c += 1
'''

# 062
'''
p_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 10
while c > 0:
    print(p_termo, end=' ')
    p_termo += razao
    c -= 1
    if c == 0:
        c = int(input('\nAcrescentar mais números na sequência: '))
'''

# 063
'''
n = int(input('Quantos termos quer? '))
a = 0
b = 1
c = 0
cont = 0
while cont < n:
    print('{}'.format(c), end=' ')
    a = b
    b = c
    c = a + b
    cont += 1
print('FIM')
'''

# 064
'''
n = total = cont = 0
while n != 999:
    n = int(input('Digite um número inteiro ou 999 para parar: '))
    if n != 999:
        total += n
        cont += 1
print('Foram digitados {} números e a soma entre eles foi {}'.format(cont, total))
'''

# 065
'''
media=soma=n=cont=0
c='S'
numeros= []
while c == 'S':
    n=int(input("Insira o numero:"))
    c=input("Deseja continuar(S/N)?").upper()
    numeros.append(n)
    cont+=1
    soma+=n
    media=(soma/cont)
print("A média é {}, o maior número foi {} e o menor {}.".format(media,max(numeros),min(numeros)))
'''

# 066
'''
cont = soma = 0
while True:
    num = int(input("Digite um valor (999 para parar): "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f"A soma dos {cont} valores foi {soma}!")
'''

# 067
'''
while True:
    n = int(input('De qual número queres ver a tabuada [negativo para finalizar]: '))
    if n < 0:
        break
    c = 1
    print('-'*11)
    while c < 11:
        print(f'{n} * {c} = {n * c}')
        c += 1
    print('-'*11)
print('Programa Encerrado!')
'''

# 068
'''
import random
med = 0
while True:
    comp = random.randint(0, 5)
    print('=-='*15)
    x =  int(input('PAR OU ÍMPAR [0 PAR / 1 ÍMPAR]: '))
    usua = int(input('DIGITE [1/5]: '))
    soma = comp + usua
    if x == 0:
        if soma % 2 == 0:
            print('-'*45)
            print(f'Você jogou {usua} e o computador {comp}. Total de {soma} DEU PAR.')
            print('-'*45)
            print('VOCÊ VENCEU! VAMOS JOGAR NOVAMENTE ...')
            med = med + 1
        else:
            print(f'Você jogou {usua} e o computador {comp}. Total de {soma} DEU ÍMPAR.')
            break
    if x == 1:
        if soma % 2 == 1:
            print('-'*45)
            print(f'Você jogou {usua} e o computador {comp}. Total de {soma} DEU ÍMPAR.')
            print('-'*45)
            print('VOCÊ VENCEU! VAMOS JOGAR NOVAMENTE ...')
            med = med + 1
        else:
            print(f'Você jogou {usua} e o computador {comp}. Total de {soma} DEU PAR.')
            break
print(f'\033[1;31mGAME OVER!\033[m Você venceu {med} vezes.')
'''

# 069
'''
pessoasMais20 = TotHomens = mulheresMenos20 = 0
while True:
    print("--" * 12)
    print("CADASTRE UMA PESSOA")
    print("--" * 12)
    idade = int(input("Idade: "))
    sexo = " "
    if idade >= 18:
        pessoasMais20 += 1
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).upper().strip()
    if sexo == "M":
        TotHomens += 1
    if sexo == "F" and idade < 20:
        mulheresMenos20 += 1
    print("--" * 12)
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar [S/N]: ")).upper().strip()
    if resp == "N":
        break
print(f"Total de pessoas com mais de pessoas com mais de 18 anos: {pessoasMais20}")
print(f"Ao todo temos {TotHomens} homem cadastrados")
print(f"E temos {mulheresMenos20} mulheres com menos de 20 anos")
'''

# 070
'''
TotCompra = maiorMil = produtoBarato = 0
barato = 100000
print("--" * 12)
print(" LOJA SUPER BARATÃO ")
print("--" * 12)
resp = ' '
c = 1
while True:
    produto = str(input("Nome do produto: "))
    valor = float(input("Preço: R$ "))
    TotCompra += valor
    if valor >= 1000:
        maiorMil += 1
    if c == 1:
        barato = valor
        produtoBarato = produto
    else:
        if barato > valor:
            barato = valor
            produtoBarato = produto
    c += 1
    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resp == "N":
        break
print(f"---------- FIM DO PROGRAMA ----------")
print(f"O total da compra foi de R${TotCompra:.2f}")
print(f"Temos {maiorMil} produto que custando mais de R$1000.00")
print(f"O produto mais barato foi {produtoBarato} que custa R${barato:.2f}")
'''

# 071
'''
valor = int(input("informe o valor a ser sacado: R$ "))
nota50 = valor // 50
valor %=  50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")
'''

# 072
'''
cont = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"]
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente. ", end='')
print(f"Você digitou o número {cont[num]}")
'''

# 073
'''
brasileirao_2026 = ["Atlético-MG", "Athletico-PR", "Bahia", "Botafogo", "Bragantino", "Chapecoense",    "Corinthians", "Coritiba", "Cruzeiro", "Flamengo", "Fluminense", "Grêmio", "Internacional",   "Mirassol",   "Palmeiras", "Remo", "Santos", "São Paulo", "Vasco", "Vitória"]
print("-=-" * 12)
print(f"Lista de times do Brasileirão: {brasileirao_2026}")
print("-=-" * 12)
print(f"Os 5 primeiros são: {brasileirao_2026[0:5]}")
print("-=-" * 12)
print(f"Os 4 ultimos são: {brasileirao_2026[16:21]}")
print("-=-" * 12)
print(f"Times em ordem alfábetica: {sorted(brasileirao_2026)}")
print("-=-" * 12)
print(f"O Corinthians está na posição {brasileirao_2026.index('Corinthians')+1}")
'''

# 074
'''
from random import randint
lista = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
organizado = (sorted(lista))
print(f'→ Os números gerados foram: {lista}.')
print(f'→ O menor número foi {organizado[0]}.')
print(f'→ O menor número foi {organizado[4]}.')
'''

# 075
'''
valores = tuple(int(input('Digite valores '))for c in range(1, 5))
print(f'O numero nove aparece {valores.count(9)} vezes')
print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição' if 3 in valores else 'Não foi digitado valor 3')
print('Valores pares digitados foram', end=' ')
print({n for n in valores if n % 2 == 0}, end=' ')
'''

# 076
'''
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40}", f" R$ {produtos[c+1]:>7.2f}")

print("="*50)
'''

# 077
'''
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end=' ')
'''

# 078
'''
valores = []
for cont in range (0, 5):
    valores.append(int(input(f'Digite um valor na posiçpão {cont}:')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor é: {max(valores)}')
print(f'O menor valor é: {min(valores)}')
for pos, v in enumerate(valores):
    if v == max(valores):
        print(f'o maior valor está na posição {pos}')
    if v == min(valores):
        print(f'O menor valor está na posição {pos}')
'''

# 079
'''
lista=[]
resposta=""
while resposta in "S":
    num=int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Esse numero ja existe")
    resposta=str(input("Deseja continuar? [S/N]")).upper().strip()
    if resposta == "N":
        break
print("==" * 12)
lista.sort()
print(f"Você digitou os valores {lista}")
'''

# 080
'''
import bisect
numbers = []
for i in range(5):
    n = int(input('Type a number: '))
    bisect.insort(numbers, n)
    print(f'Number {n} included in position {numbers.index(n)}')
print(f'Numbers typed: numbers')
'''

# 081
'''
lista = []
resp = ""
while resp in "S":
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor repetido. Não vou adicionar")
    resp = str(input("Quer continuar [S/N]: ")).upper().strip()
    if resp == "N":
        break
print("==" * 14)
print(f"Você digitou {len(lista)} elementos")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não foi encontrado na lista")
'''

# 082
'''
num = [] # Lista Completa
pares = [] # Pares
impares = [] # Ímpares
resp = ''
while resp in "S":
    valor = int(input("Digite um número: "))
    num.append(valor)
    if num % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    resp = str(input("Você quer continuar [S/N]: ")).upper().strip()
    if resp == 'N':
        break
print("==" * 14)
print(f"A lista completa é {num}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")
'''

# 083
'''
expr = str(input('Digite a expressão: '))
if expr.count('(') == expr.count(')'):
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida')
'''

# 084
'''
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    resp = str(input("Quer continuar [S/N]: "))
    if resp in 'Nn':
        break
print("-=" * 15)
print(f"Os dados foram {princ}")
print(f"Ao todo, você cadastrou {len(princ)} pessoas")
'''

# 096
'''
# Função
def calcular_area(larg, comp):
    area = larg * comp
    print(f"A área de um terreno de {larg} x {comp} é de {area}m²")


# Programa principal
print("Controle de terrenos")
print("--" * 13)
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
calcular_area(l, c)
'''

# 097
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
'''

# 098
'''
from time import sleep
# Função
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print("--" * 30)
    print(f"A contagem de {i} até {f} de {p} em {p}")
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.5)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.5)
            cont -= p
        print("FIM!")

# Programa principal
contador(1, 10, 1)
contador(10, 0 , 2)
print("--" * 30)
print("Agora é a sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
'''

# 099
'''
from time import sleep
# Função
def maior(* numeros):
    print("--" * 30)
    print("Analisando os valores passados...")
    print(f"{numeros} Foram informados {len(numeros)} valores ao todo")
    print(f"O maior valor informado foi {max(numeros)}")


# Programa principal
maior(5, 4, 7, 3, 1)
maior(8, 9, 2, 7)
maior(0, 6, 5)
maior(10, 9)
maior(1)
'''

# 100
'''
from random import randint
# Função
def sortear_somar(* lista_sorteada):
    print("--" * 30)
    print(f"Sorteando os 5 valores da lista: {lista_sorteada} PRONTO!")
    addPar = 0
    for numero in lista_sorteada:
        if numero % 2 == 0:
            addPar += numero
    print(f"Somando os valores pares de {lista_sorteada}, temos {addPar}")

# Programa principal
lista_sorteada = []
for c in range(0, 5):
    numero = randint(0, 10)
    lista_sorteada.append(numero)
    c += 1
sortear_somar(* lista_sorteada)
'''

# 101
'''
# Função
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif 16 <= idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"


# Página principal
nasc = int(input("Ano de nascimento: "))
print(voto(nasc))
'''

# 102
'''
def fatorial(n, show=False):
    """
    -> Calcula o fatorial do número digitado.
    :param n: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: Retorna o valor de n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')
        f *= c
    return f

# Programa principal
print(fatorial(5, show=True))
'''

# 103
'''
# Função
def ficha(nome, gols):
    if not nome:
        nome = '<desconhecido>'
    if not gols:
        gols = 0
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")



# Programa principal
nome = str(input("Digite o nome do jogador: "))
gols = int(input("Digite a quantidade de gols: "))
ficha(nome, gols)
'''

# 104
'''
# Função
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;031mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor



# Programa principal
n = leiaInt('Digite um número: ')
print(f"Você acabou de digitar o número {n}")
'''

# 105
'''
def notas(*num, sit=False):
    cont = maior = menor = media = total = 0
    for c in num:
        cont += 1
        if c > maior:
            maior = c
        if c < menor or cont == 1:
            menor = c
        total += c
    media = total / cont
    if sit:
        print('A situação da turma é: ', end='')
        if media > 7:
            print('Boa!')
        elif media > 5:
            print('Rasoável')
        else:
            print('Ruim!')

    return print(f'A nota total da turma é {total}, maior nota é {maior}, a menor nota é {menor} e a media da turma é {media}')


resp = notas(8, 6, 5, 9, 6, 9, sit=True)
print(resp)
'''

# 106
