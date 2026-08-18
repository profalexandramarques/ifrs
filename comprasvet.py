#Compras Veteriária PetIFRS
#Dados do Produto
codigo  = int(input("Digite o código do produto: "))
nome    = input("Digite o nome do produto: ")
tamanho = int(input("Digite o tamanho do produto (1/7/15 kg): "))
qtde    = int(input("Digite a quantidade: "))
valor   = float(input("Digite o valor do produto: "))
brinde  = input("Ganha brinde (1 - Sim, 0 - Não): ")
valor_total = qtde * valor
print("\n====== PetIFRS ======")
print("Nome:",nome)
print("Código:",codigo)
print("Tamanho:",tamanho,"kg")
print("Quantidade:",qtde)
print("Valor unitário: R$ {:.2f}".format(valor))
print("Brinde:",brinde)
print("Valor total a pagar: R$ {:.2f}".format(valor_total))
