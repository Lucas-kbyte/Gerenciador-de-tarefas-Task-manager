import time
from tarefas import lista_tarefas
from tarefas import ver_tarefa
from tarefas import adicionar_lista
from tarefas import concluir_lista
from tarefas import carregar_dados
from tarefas import remover_tarefa

carregar_dados()

while True:
    print("———————————————— Gerenciador de tarefas ————————————————")
    time.sleep(0)
    print("1 - Ver tarefas")
    time.sleep(0)
    print("2 - Adicionar tarefa")
    time.sleep(0)
    print("3 - Concluir tarefa")
    time.sleep(0)
    print("4 - Remover tarefa")
    time.sleep(0)
    print("5 - Sair")
    time.sleep(0)
    print("————————————————————————————————————————————————————————")
    try:
        escolha = input("Digite sua escolha: ")
    except:
        print("Algo deu errado, tente de novo")

    match escolha:
        case "1":
            ver_tarefa()
        case "2":
            adicionar_lista()
        case "3":
            concluir_lista()
        case "4":
            remover_tarefa()
        case "5":
            print("Parando o programa, porfavor aguarde um pouco")
            time.sleep(0)
            break
        case _:
            print("Ops, algo deu errado, tente denovo")
