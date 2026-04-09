num = int(input('Digite um número entre 0 e 20: '))
ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
#while num > 20 or num < 0:
    #print('Número fora do intervalo. Tente novamente!')
    #num = int(input('Digite um número entre 0 e 20: '))
#print(f'Você digitou o número {ext[num]} \n')

while True:
    if num > 20 or num < 0:
        print('Você digitou errado. Tente novamente')
        num = int(input('Digite um número entre 0 e 20: '))
    else:
        break
print(f'Você digitou o número {ext[num]}')