#Algoritmo para verificar a frequência cardiaca e respiratória
print("==== Saúde Cardíaca e Respiratória ====")
#Ler da tela as informações
nome = input("😷 Digite o nome do paciente: ")
peso = float(input("Digite o peso do paciente: "))
altura = float(input("Digite a altura do paciente: "))
cardiaca = int(input("❤️ Digite a frequência cardíaca em bpm: "))
respiratoria = int(input("🩺 Digite a frequência respiratória em ipm: "))
#Comando condicional
#Verifica a frequencia cardiaca
if(cardiaca > 100):
    print("Taquicardia")
elif(cardiaca >= 60):
    print("Normal")
else:
    print("Bradicardia")

#Verifica a frequencia respiratória
if(respiratoria > 20):
    print("Taquipneia")
elif(respiratoria >= 12):
    print("Normal")
else:
    print("Bradipneia")