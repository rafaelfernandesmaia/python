tarefas = []

def mostrar_tarefa():
    if not tarefas:
        print('Nenhuma tarefa na lista')
    else:
        print('\nTarefas: ')
        for i, tarefas in enumerate(tarefas, i):
            status = '✓' if tarefas['concluída'] else '✗'
            print(f'{i}. [{status}] {tarefas['descrição']}')

def adicionar_tarefas():
    desc = str(input('Digite uma descrição da tarefa: '))
    tarefas.append({'descrição': {desc}, 'concluída': False})
    print('Tarefa adicionada!')
    

def marcar_concluido():
    mostrar_tarefa()
    if tarefas:
        n = int(input('Digite o número da tarefa que você concluiu: '))
        if 1 <= n <= len(tarefas):
            tarefas[n-1]['concluída'] = True
            print('Tarefa marcada como concluída!')
        else:
            print('Número inválido!')


while True:
    print('\nO que você deseja fazer?')
    print('1 - Mostrar tarefa')
    print('2 - Adicionar tarefa')
    print('3 - Marcar tarefa como concluído')
    print('0 - Sair do programa')

    escolha = input('Digite uma opção: ')

    if escolha == '1':
        mostrar_tarefa()
    elif escolha == '2':
        adicionar_tarefa()
    elif escolha == '3':
        marcar_concluido()
    elif escolha == '0':
        print('Saindo...')
        break
    else:
        print('Opção Inválida. Digite uma opção válida!')