print('==' * 13)
print('   10 TERMOS DE UMA PA    ')
print('==' * 13)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c} ', end='→ ')
print('ACABOU')