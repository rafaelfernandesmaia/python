v = float(input('Qual é a velocidade do carro? '))
if v > 80:
    print('MULTADO, você ultrapassou a velocidade máxima permitida de 80km/h')
    multa = (v-80) * 7
    print(f'O valor da multa que você tem que pagar será {multa}')
print('Tenha um bom dia, diriga com serugança!')