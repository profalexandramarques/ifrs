#Verificar frequencia cardiaca e respiratória
print("==== 🏥 Saúde do Paciente 🩺 ====")
nome = input("😷 Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
altura = float(input("Digite a altura do paciente: "))
peso = float(input("Digite o peso do paciente: "))
cardiaca = int(input("❤️  Digite a frequência cardíaca em bpm: "))
respira = int(input("🩺  Digite a frequência respiratória em ipm: "))
#Comando condicional
#Verifica a frequencia cardiaca
if(cardiaca > 100):
    print("Taquicardia")
elif(cardiaca >= 60):
    print("Normal")
else:
    print("Bradicardia")
#Verifica a frequencia respiratória
if(respira > 20):
    print("Taquipeia")
elif(respira >= 12):
    print("Normal")
else:
    print("Bradipneia")