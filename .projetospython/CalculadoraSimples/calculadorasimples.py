# Calculadora Simples - Projeto com Python

# Fazer uma calculadora simples que realiza as seguintes operações básicas: adição, subtração, multiplicação, divisão

def cabeçalho():
    print('-' * 25)
    print('CALCULADORA SIMPLES'.center(25))
    print('-' * 25)
    print('Menu - Calculadora'.center(25))
    print('-' * 25)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
cabeçalho()
print('[ 1 ] Somar\n[ 2 ] Subtração\n[ 3 ] Multiplicação\n[ 4 ] Divisão\n[ 5 ] Sair do Programa')
print('-' * 25)
while True:
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print("Você escolheu Somar!")
        soma = n1 + n2
        print(f"A soma de {n1} e {n2} é igual a {soma}")
        print('-' * 25)
    elif opcao == 2:
        print('Você escolheu Subtração!')
        subtracao = n1 - n2
        print(f'A subtração de {n1} e {n2} é igual a {subtracao}')
        print('-' * 25)
    elif opcao == 3:
        print('Você escolheu Multiplicação!')
        mult = n1 * n2
        print(f'A multiplicação de {n1} e {n2} é igual a {mult}')
        print('-' * 25)
    elif opcao == 4:
        print('Você escolheu Divisão!')
        divi = n1 / n2
        print(f'A divisão de {n1} e {n2} é igual a {divi}')
        print('-' * 25)
    elif opcao == 5:
        print('Você escolheu Sair do Programa!')
        print('Finalizando o projeto...')
        break
    else:
        print('Opção Inválida. Tente inserir uma opção válida!')