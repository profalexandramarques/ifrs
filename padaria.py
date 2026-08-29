#Padaria IFRS
print("=== Padaria IFRS ===")
print("=== Cardápio     ===")
print("=== 1 - Café: 4,50\n2 - Bolo: 8,00\n3 - Refri: 2,50\n4 - Pastel: 5,00 ===")
nome = input("Digite o nome do cliente: ")
codigo = int(input("Digite o código do produto: "))
#valor = float(input("Digite valor do produto: "))
if(codigo == 1):
    valor = 4.5
qtde = int(input("Digite a qtde do produto: "))
#Cálculo Valor Total
valor_total = qtde * valor
print("O valor total a pagar R$ {:.2f}".format(valor_total))
