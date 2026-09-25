#Agência de Turismo
import os
import time
#Lista de Pacotes de Viagem usando dicionário
pacotesviagem = [
    {
        "destino": "Paris",
        "valor": 8000
    },
    {
       "destino": "Rio de Janeiro",
        "valor": 948
    },
    {
      "destino": "Natal",
      "valor": 1755
    }]

#Funções
def limpar_tela():
     os.system('cls')

def menu():
    print("==== Menu Principal ====")
    print("1. Comprar pacote de viagem. \n2. Calcular valor mensal")
    print("3. Listar os pacotes de viagem. \n9. Sair")

def comprarpacote():
    print("Pacote de Viagem comprado com sucesso!")

def calcularvalor():
    print("Valor calculado com sucesso!")

def listarpacotes():
    print("==== Pacotes de Viagem ====")
    #Mostrar os dados na tela
    for pacote in pacotesviagem:
        destino  = pacote["destino"]
        valor    = pacote["valor"]        
        print(f"🗺️  {destino} a partir de R$ {valor:.2f}. ")
    print("===========================")

#Programa Principal
limpar_tela()
print("==== Agência de Turismo ====")
opcao = 0
while (opcao != 9):
    menu()
    opcao = int(input("Digite a operação: "))
    match opcao:
        case 1:
            comprarpacote()
        case 2:
            calcularvalor()
        case 3:
            listarpacotes()
        case 9:
            print("Boa viagem. Volte sempre!")
        case _:
            print("Operação inválida!")
    time.sleep(2)