casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do financiador: R$ '))
anos = int(input('Em quantos anos ele vai financiar: '))
prestacao = casa / (anos * 12)
minimo = salario * 0.3
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos, a prestação será de {prestacao:.2f}')
if prestacao <= minimo:
    print('O empréstimo pode ser CONCEDIDO!')
else:
    print('O empréstimo foi NEGADO!')