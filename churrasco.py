#Dicionario do Churrasco da Semana Farroupilha
tabela = {
    "Alface":4.99,
    "Tomate":8.99,
    "Batata":2.99,
    "Costela":49.90,
    "Carvão":19.90,
    "Sal grosso":2.99,
    "Bebida":13.90,
    "Salsichão":18.99
}

#Incluir mais uma chave valor
tabela["Pão"] = 8.99
print(tabela)

#Mostrar as chaves
print(tabela.keys())

#Mostrar os valores
print(tabela.values())

print("====== Churrasco ======")
for produto, preco in tabela.items():
    print(f"{produto:<12}  R$ {preco:.2f}")