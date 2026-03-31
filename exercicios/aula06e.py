n1 = float(input('Primeiro nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}')
if media >= 7.0:
    print('O aluno está APROVADO!')
elif 7 > media >= 5.0:
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO')