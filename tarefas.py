import time
import os
#simulador de tarefas
#Lista de tarefas vazia
tarefas = []

# Funções 
def limpar_tela():
     os.system('cls')

def menu():
    print("==== 📋 GERENCIADOR DE TAREFAS 📋====")
    print("1 - 📋 Adicionar uma tarefa")
    print("2 - 📋 Listar todas as tarefas")
    print("3 - 📋 Excluir uma tarefa")
    print("4 - 📋 Concluir tarefa")
    print("5 - 📋 Ordenar a lista de tarefas")
    print("9 - Sair")

    
def incluir():
    nova_tarefa = input("Digite a nova tarefa: ")
    if nova_tarefa not in tarefas:
        tarefas.append(nova_tarefa)
        print("📋 Tarefa incluída com sucesso!")
    else:
        print("A tarefa já existe na lista!")

def listar():
    print("==== 📋 Lista de Tarefas 📋 ====")
    i = 1
    for tarefa in tarefas:
        print(i," - ",tarefa)
        i +=1
    print("================================")

def excluir():
    listar()
    num = int(input("Digite o número da tarefa a excluir: "))
    tarefas.pop(num)
    print(f"Tarefa excluída com sucesso!")

def concluir():
    listar()
    num = int(input("Digite o número da tarefa a concluir: "))
    tarefas[num] = tarefas[num] + " X"
    print("Tarefa concluída com sucesso!")

def ordenar():
    tarefas.sort()
    print("Lista de tarefas ordenada com sucesso!")

#Programa Principal
limpar_tela()
opcao = 0
while (opcao !=9):
    menu()    
    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            incluir()
        case 2:
            listar()
        case 3:
            excluir()
        case 4:
            concluir()
        case 5:
            ordenar()
        case 9:
            print("Saindo do gerenciador de tarefas...")
        case _:
            print("Opção inválida! Tente novamente.")
    time.sleep(1)