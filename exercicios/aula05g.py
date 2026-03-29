sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    novosal = sal * 1.15
else:
    novosal = sal * 1.10
print(f'Quem ganhava R$ {sal:.2f} passa a ganhar R${novosal:.2f}')