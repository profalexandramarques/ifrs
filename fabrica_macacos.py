#Fabrica de Bananas Tech
#Lista de Macacos com dicionario
listamacacos=[
    {
    "nome": "Chico",
    "idade":5,
    "bananas":15
},
{
    "nome": "Ana",
    "idade":3,
    "bananas":10
},
{
    "nome": "Beto",
    "idade":7,
    "bananas":2
} ]
print("==== Fábrica de Bananas Tech ====")
#Mostrar os macacos 
for macaco in listamacacos:
    print(f"{macaco["nome"]} tem {macaco["idade"]} anos e possui {macaco["bananas"]} bananas")