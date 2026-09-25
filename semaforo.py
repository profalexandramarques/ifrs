#Simular o semáforo
import time
import random
import os
'''
1 - Siga    - Verde
   2 - Atenção - Amarelo
   3 - Pare Vermelho
'''
#Funções
def limpar_tela():
     os.system('cls')

#Programa Principal
limpar_tela()
sinal = 3
print("==== 🚦 Semáforo 🚦 ====")
for i in range(1,11):    
    sinal = random.randint(sinal,3)
    match sinal:
        case 1: 
            print("🟢 - 1 - Siga")            
            sinal = 3 
        case 2:
            print("🟡 - 2 - Atenção")
            sinal = 1
        case 3:
            print("🔴 - 3 - Pare")
            sinal = 2
    
    time.sleep(1)