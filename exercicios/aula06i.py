print('========== LOJAS RAFAEL ==========')
compra = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    valor = compra * 0.90
    print(f'Sua compra de {compra:.2f} vai custar R${valor:.2f} no final')
elif opcao == 2:
    valor = compra * 0.95
    print(f'Sua compra de {compra:.2f} vai custar R${valor:.2f} no cartão')
elif opcao == 3:
    valor = compra
    parcela = valor / 2
    print(f'Sua compra vai ser parcelada em 2x de R${parcela:.2f} SEM JUROS')
    print(f'Sua compra de {compra:.2f} vai custar {valor:.2f} no final')
elif opcao == 4:
    valor = compra * 0.80
    totalparcela = int(input('Quantas parcelas: '))
    parcela = valor / totalparcela
    print(f'Sua compra de {compra:.2f} será parcelada em {totalparcela:.2f}x de R${parcela:.2f} COM JUROS')
    print(f'Sua compra de {compra:.2f} vai custar {valor:.2f} no final')
else:
    print('Opção inválida de pagamento. Tente novamente.')
