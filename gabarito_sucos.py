#Gabarito da Prova - Loja de Sucos
import os
import time
#Lista de Sucos
sucos = ["laranja","uva"]

#Funções
def limpar_tela():
     os.system('cls')

def menu():
    print("==== Menu Principal Sucos da Naty ====")
    print("1 - Cadastrar um suco")
    print("2 - Ver cardápio")
    print("3 - Fazer o pedido")
    print("9 - Sair")
    print("======================================")

def cadastrar_suco():
    suco = input("Digite o nome do suco: ")
    if suco in sucos: 
        print("Suco já cadastrado!")
    else:
        sucos.append(suco)
        print("Suco cadastrado com sucesso!")

def ver_cardapio():
    print("==== Cardápio de Sucos ====")
    print("==== Sucos R$ 8,00     ====")
    i = 1
    for suco in sucos:
        print(i," - ",suco)
        i += 1
    print("===========================")

def fazer_pedido(valor):
    ver_cardapio()
    suco = input("Digite o nome do suco: ")    
    if suco in sucos:
        nome = input("Digite o seu nome: ")    
        qtde = int(input("Digite a quantidade de sucos: "))
        valortotal = qtde * valor
        print("==== Pedido de Suco ====")
        print(f"{nome} o valor total a pagar pelo suco de {suco} é {valortotal:.2f}!")
        print("========================")
    else:
        print("Suco não cadastrado!")


#Programa Principal
limpar_tela()
op = 0
valor = 8.00
while op != 9:
    menu()
    op = int(input("Digite a opção do Menu: "))
    match op:        
        case 1:
            cadastrar_suco()
        case 2:
            ver_cardapio()
        case 3:
            fazer_pedido(valor)
        case 9:
            print("Volte sempre!")
        case _:
            print("Opção inválida!")


    time.sleep(2)    

