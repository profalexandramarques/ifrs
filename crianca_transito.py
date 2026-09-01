#Criança no banco da frente
idade  = int(input("Digite a idade da criança: "))
altura = float(input("Digite a altura da criança: "))
#Verifica se pode estar no banco da frente
if(idade >= 18):
   print("Adulto pode ir no banco da frente!") 
elif(idade >= 10 and altura >=1.45):
    print("Criança pode ir no banco da frente!")
else:
    print("Criança não pode ir no banco da frente!")

print("Use o cinto de segurança!")