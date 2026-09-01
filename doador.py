#Banco de Sangue do IFRS
nome   = input("Digite o nome do doador: ")
sangue = input("Digite o tipo sanguíneo: ")
idade  = int(input("Digite a idade: "))
peso   = float(input("Digite a peso: "))
#Verifica se é doador
if(idade >= 18 and peso >= 50):
    print("Você pode doar sangue!")
else:
    print("Você não pode doar sangue!")