d = float(input('Qual é a distância da viagem: '))
print(f'Você está prestes a começar uma viagem de {d} km')
if d <= 200:
    preco = d * 0.50
else:
    preco = d * 0.45
print(f'O valor que você irá pagar nessa viagem é R${preco:.2f}')