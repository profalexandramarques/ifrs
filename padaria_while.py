#Padaria IFRS
print("==== Padaria IFRS ===")
codigo = 0
valor_total = 0
nome = input("Digite o nome do cliente: ")
while(codigo != 9):    
   print("==== Cardápio ===")
   print("1 - Café - 4.50\n2 - Bolo - 8.00\n3 - Pastel - 5.00\n4 - Refri - 2.50\n9 - Fecha conta")   
   codigo = int(input("Digite o código do produto: "))
   if(codigo !=9):
      qtde = int(input("Digite a qtde do produto: "))
      if(codigo == 1):
         valor = 4.5
      elif(codigo == 2):
         valor = 8.0
      elif(codigo == 3):
         valor = 5.0
      elif(codigo == 4):
         valor = 2.5
      else:
         valor = 0
      #Calculo do subtotal por item
      subtotal = qtde * valor
      valor_total = valor_total + subtotal
      print("Subtotal é R$ {:.2f}".format(subtotal))
#Escrever o valor total
print("O valor total a pagar é R$ {:.2f}".format(valor_total))