import os
#Trabalhando com funções
def limpartela():
    os.system('cls')

#Função sem parametro e sem retorno
def olamundo():
    print("Ola Mundo!")

#Função com parâmetros
def mensagem(msg):
    print(msg)

#Função com parâmetros e retorno
def soma(a,b):    
    return(a + b)

#Programa Principal
limpartela()
olamundo()
mensagem("Boa noite!")
n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
r = soma(n1,n2)
print("A soma é",r)

