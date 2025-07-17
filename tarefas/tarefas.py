import defs

lista = []
task = {}
## Criar um programa que permita cadastrar tarefas do dia com status de conclusão.

defs.lines()
print('To Do List')
defs.lines()

defs.menu()

while True:
    option = int(input('Select the desired option: '))
    match option:
        case 1: #adicionar tarefa
            name = input('Enter the name of the desired task: ')
            status = int(input('Select task status: \n1 for pendant. \n2 for completed \n-  '))
            if status == 1:
                status = 'pendant'
            elif status == 2:
                status = 'completed'
            task = {
                "task_name": name,
                "status": status
            }
            lista.append(task)
            last = lista[-1]
            print(f'Task {last["task_name"]} with status {last["status"]} added successfully')
        case 2: #alterar status
            #print('Which task do you want to change?')
            if lista[task] == None:
                print('Void list')
            else:
                for task in lista[task]:
                    print(f'{task}')
