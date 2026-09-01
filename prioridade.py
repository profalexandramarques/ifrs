#Verificar o atendimento prioritário
print("=== Sistema de Saúde ===")
nome  = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
#Comando condicional
if(idade >= 65):
    print("Atendimento prioritário!")
else:
    print("Atendimento normal!")