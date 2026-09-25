import os
import time
#Simular um caixa eletrônico
movimentacoes = ["Saldo inicial R$ 1000.00"]
#Funções
def limpar_tela():
     os.system('cls')

def menu():
    print("===== Menu Principal =====")
    print("1 - Sacar 💵 \n2 - Depositar 💰\n3 - Ver Saldo 🧾 ")
    print("4 - Pagar Boleto 💵 \n5 - Extrato 🧾 \n9 - Sair")

def sacar(saldo):
    valor = float(input("Digite o valor: "))
    if(valor <= saldo):
        saldo = saldo - valor
        movimentacoes.append("Saque R$ "+str(valor))
        print("Saque realizado com sucesso!")
    else:
        print("Saque não realizado. Saldo insuficiente!")
    return saldo

def depositar(saldo):
    valor = float(input("Digite o valor: "))
    saldo = saldo + valor
    movimentacoes.append("Depósito R$ "+str(valor))
    print("Depósito realizado com sucesso!")
    return saldo

def versaldo(saldo):
    print("O saldo atual é R$ {:.2f}".format(saldo))

def pagarboleto(saldo):
    valor = float(input("Digite o valor: "))
    if(valor <= saldo):
        descricao = input("Digite a descrição do boleto: ")
        saldo = saldo - valor
        movimentacoes.append("Boleto "+descricao+" R$ "+str(valor))
        print("Boleto pago com sucesso!")
    else:
        print("Boleto não pago. Saldo insuficiente!")
    return saldo

def extrato():
    print('====== 💵 Extrato 💵 ======')
    for descricao in movimentacoes:
        print(descricao)    
    print('============================')

#Programa Principal
limpar_tela()
saldo = 1000
op = 0
print('====  🏧 Bank IFRS 🏧 ====')
while(op != 9):
    menu()
    op = int(input('Digite a operação bancária: '))
    match op:
        case 1:
            saldo = sacar(saldo)
        case 2:
            saldo = depositar(saldo)
        case 3:
            versaldo(saldo)
        case 4:
            saldo = pagarboleto(saldo)
        case 5:
            extrato()
            versaldo(saldo)
        case 9:
            print("💵 Volte sempre!")
        case _:
            print("Operação inválida!")
    time.sleep(3)