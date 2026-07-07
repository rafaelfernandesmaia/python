tarefas = []

while True:
    print('\nO que você deseja fazer?')
    print('1 - Mostrar tarefa')
    print('2 - Adicionar tarefa')
    print('3 - Marcar tarefa como concluído')
    print('0 - Sair do programa')

    escolha = int(input('Digite uma opção: ')).strip()[0]

    if escolha == 1:
        mostrar_tarefa()
    elif escolha == 2:
        adicionar_tarefa()
    elif escolha == 3:
        marcar_concluido()
    elif escolha == 0:
        print('Saindo...')
        break
    else: