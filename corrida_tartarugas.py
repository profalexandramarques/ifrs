#Corrida das tartarugas
import turtle as t
import random

#Cria um dado com 6 lados
dado = [1,2,3,4,5,6]
t.title("Corrida das Tartaruga")
#Tartaruga 1
player_one = t.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
#Tartaruga 2
player_two = player_one.clone()
player_two.color("purple")
player_two.penup()
player_two.goto(-200,-100)
#Casas
player_one.goto(250,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(250,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

for i in range(20):
    if player_one.pos() >= (250,100):
        print("Player Green Venceu!")
        break
    elif player_two.pos() >= (250,-100):
        print("Player Purple Venceu!")
        break
    else:            
        player_one_turn = input("Pressione 'Enter' para jogar o dado: ")
        dado_sorteado = random.choice(dado)
        print(dado_sorteado)
        print("O resultado do dado é: ")
        print(dado_sorteado)
        print("O número de etapas será: ")
        print(20*dado_sorteado)
        player_one.fd(20*dado_sorteado)
        player_two_turn = input("Pressione 'Enter' para jogar o dado: ")
        dado_sorteado = random.choice(dado)
        print("O resultado do dado é: ")
        print(dado_sorteado)
        print("O número de etapas será: ")
        print(20*dado_sorteado)
        player_two.fd(20*dado_sorteado)
t.done()
