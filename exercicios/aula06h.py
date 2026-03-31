kg = float(input('Qual é o seu peso? (Kg) '))
m = float(input('Qual é a sua altura? (m)'))
imc = kg / m**2
print(f'O IMC dessa pessoa é de {imc}')
if imc < 18.5:
    print('Você está Abaixo do Peso')
elif imc < 25:
    print('Você está Peso ideal')
elif imc < 30:
    print('Você está Sobrepeso')
elif imc < 40:
    print('Você está em Obesidade')
else:
    print('Você está em Obesidade mórbida')