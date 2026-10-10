#Árvore de Natal 
ponteira = '🌟'
estrela = '⭐'
espacos = 11
print(' '*espacos+ponteira)
for i in range(1,11):    
    print(' '*espacos+estrela*i)
    espacos = espacos - 1
