import time
import json
import os
lista_tarefas = []


def salvar_dados():
    with open("Gerenciado de tarefas.json", "w") as arquivo:
        json.dump(lista_tarefas, arquivo)

def ver_tarefa():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not lista_tarefas:
        print("\nSua lista está vazia.")
    else:
        print("\nSuas Tarefas:")
        for i, item in enumerate(lista_tarefas, 1):
            simbolo = "[X]" if item["concluida"] else "[ ]"
            
            print(f"{i}. {simbolo} {item['tarefa']}")


def adicionar_lista():
    os.system('cls' if os.name == 'nt' else 'clear')
    adicione_tarefa = input("Olá, digite aqui a tarefa que gostaria de colocar\n")
    if adicione_tarefa.strip():
        lista_tarefas.append({"tarefa": adicione_tarefa, "concluida": False})
        print(f"Tarefa '{adicione_tarefa}' adicionada com sucesso!")
    else:
        print("Erro: A tarefa não pode estar vazia.")
    salvar_dados()

def concluir_lista():
    ver_tarefa() 
    
    if not lista_tarefas:
        return
    try:
        indice = int(input("\nDigite o número da tarefa que deseja concluir: "))
        
        posicao = indice - 1
        
        if 0 <= posicao < len(lista_tarefas):
            lista_tarefas[posicao]["concluida"] = True
            print(f"\nTarefa '{lista_tarefas[posicao]['tarefa']}' marcada como concluída! [X]")
        else:
            print("\nErro: Esse número de tarefa não existe.")
            
    except ValueError:
        print("\nErro: Por favor, digite um número válido.")

def carregar_dados():
    global lista_tarefas
    try:
        with open("Gerenciado de tarefas.json", "r") as arquivo:
            lista_tarefas = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_tarefas = []
carregar_dados()

def remover_tarefa():
    os.system('cls' if os.name == 'nt' else 'clear')
    ver_tarefa() 
    
    if not lista_tarefas:

        input("\nPressione Enter para voltar ao menu...")
        return 

    try:
        indice = int(input("\nDigite o número da tarefa que deseja remover: "))
        posicao = indice - 1
        
        if 0 <= posicao < len(lista_tarefas):
            removida = lista_tarefas.pop(posicao)
            print(f"\nSucesso: Tarefa '{removida['tarefa']}' foi removida")
        else:
            print("\nErro: Esse número de tarefa não existe na lista.")
            
    except ValueError:
        print("\nErro: Por favor, digite apenas números.")
    
    input("\nPressione Enter para continuar...")


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
