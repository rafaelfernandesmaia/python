a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor digitado foi {maior}')
print(f'O manor valor digitado foi {menor}')
