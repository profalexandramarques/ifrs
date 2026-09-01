#PDV
import time
print("=== Sistema PDV ===")
opcao = 0
while(opcao !=9):
    print("=== Menu Principal ===")
    print("1 - Cadastro do produto\n2 - Emitir NF-e \n3 - Cancelar Venda\n4 - Pedido de Venda\n9 - Sair")
    opcao = int(input("Digite a opção: "))
    if(opcao == 1):
        print("Produto cadastrado com sucesso!")
    elif(opcao == 2):
        print("NF-e emitida com sucesso!")
    elif(opcao == 3):
        print("Venda cancelada com sucesso!")
    elif(opcao == 4):
        print("Pedido de Venda emitido com sucesso!")
    elif(opcao == 9):
        print("Volte Sempre!")
    else:
        print("Opção inválida!")
    time.sleep(5)