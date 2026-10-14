#Jogo da Forca
import random
import time
#Cria uma lista de palavras
palavras = ["python","computador","estudo","frutas","macaco","banana","jogo"]

#Funções
def mostrar_forca(erros):
    print("===== Forca ====")
    match erros:
       case 0:
          print("""
           ------
           |    |
                |
                |
                |
        --------- """)
       case 1: # 1 erro (Cabeça)
         print("""
          ------
           |   |
           O   |
               |
               |
        --------- """)
       case 2: # 2 erros (Tronco)
            print("""
             ------
             |    |
             O    |
             |    |
                  |
            --------- """)
       case 3: # 3 erros (Braço esquerdo)
            print("""
           ------
           |    |
           O    |
          /|    |
            |
        --------- """)
       case 4: # 4 erros (Braço direito)
            print("""
           ------
           |    |
           O    |
          /|\\   |
                |
        --------- """)
       case 5: # 5 erros (Perna esquerda)
         print("""
           ------
           |    |
           O    |
          /|\\   |
          /     |
        --------- """)
       case 6: # 6 erros (Perna direita - Fim do jogo)
            print("""
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
        --------- """)

   
#Programa Principal
#Escolhe uma palavra dentro de uma lista
palavra_sorteada = random.choice(palavras).upper()
vidas = 6
acertos = []
erros = 0
print("===== 🎮 Jogo da Forca 🎮=====")
while vidas > 0:
    senha = "" 
    for letra in palavra_sorteada:
        if letra in acertos:
           senha += letra
        else:
           senha += "_"   
    print(f"Palavra {senha}:")

    if senha == palavra_sorteada:
        print("🎉 Você acertou!")
        break      

    tentativa = input("Digite uma letra: ").upper().strip()
    if tentativa in acertos:
        print("⚠️ Você já tentou essa letra!")
    else: 
        if tentativa in palavra_sorteada:
           acertos.append(tentativa)
           print("🎉 Você acertou!")
        else:
           erros +=1
           vidas -=1
           print("Você errou!",erros)
    
    
    print("\n","💜"*vidas)
    mostrar_forca(erros)
    time.sleep(1)

if vidas == 0:
    print("\n💀 Game Over! Suas vidas acabaram.")
    
print(f"A palavra sorteada foi: {palavra_sorteada}")