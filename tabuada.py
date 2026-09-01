#Tabuada
n1 = int(input("Digite um número: "))
print("=== Tabuada",n1,"===")
for i in range(1,11):
    resultado = i * n1
    print(n1, "X", i,"=",resultado)