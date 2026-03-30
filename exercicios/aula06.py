nome = str(input('Digite seu nome: '))
if nome == 'Rafael':
    print('Que nome bonito você tem')
elif nome == 'Renato' or nome == 'Allan' or nome == 'Neymar':
    print('Você é uma lenda!!')
elif nome in 'Maria Sofia Lara Beatriz':
    print(f'Você tem um belo nome feminino')
else:
    print(f'Seu nome é bem comum')
print(f'Tenha um bom dia, {nome}!')