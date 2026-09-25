#Classificação do Uber aleatória
import random
soma = 0
for i in range(1,11):
    estrela = random.randint(1,5)
    soma = soma + estrela
    print("⭐"*estrela)

#Calcular a média de estrelas
media = soma/10
print("Pontuação {:.2f} estrelas".format(media))