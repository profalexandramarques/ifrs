import os
#Reino do Kod
listafrutas = ["laranja","banana","maça"]
#Funções
#Trabalhando com funções
def limpartela():
    os.system('cls')
#Menu principal
def menu():
    print("=== Menu Principal ===")
    print("1 - Adicionar fruta\n2 - Excluir fruta\n3- Ordenar a lista")
    print("4 - Mostrar as frutas\n9 - Sair")

#Incluir na lista
def inserir():
    fruta = input("Digite o nome da fruta: ")
    if fruta not in listafrutas: 
        listafrutas.append(fruta)
        print("Fruta inserida com sucesso!")      
#Excluir da lista
def excluir():
    fruta = input("Digite o nome da fruta: ")
    if fruta in listafrutas: 
        listafrutas.remove(fruta)
        print("Fruta removida com sucesso!")
    else:
        print("Fruta não encontrada!")
#Ordenar a lista
def ordenar():
    listafrutas.sort()
#Mostrar as frutas da lista
def listar():
    for fruta in listafrutas:
        print(fruta)
#Programa Principal
limpartela()
op = 0
while (op!=9):
    menu()
    op = int(input("Digite a opção: "))
    match op:
        case 1:
            inserir()
        case 2:
            excluir()
        case 3:
            ordenar()
        case 4: 
            listar()
        case 9:
            print("Volte sempre!")
        case _:
            print("Operação inválida!")