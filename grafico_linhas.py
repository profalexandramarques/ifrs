import matplotlib.pyplot as plt

# Dados de exemplo
meses = ["Jul", "Ago", "Set", "Out", "Nov", "Dez"]
vendas = [120, 150, 180, 200, 230, 260]

# Criando o gráfico de linha
plt.plot(meses, vendas, marker='o', 
         color='#9e2c6a', linewidth=3)
plt.title('Evolução das Vendas - 2º Semestre', fontsize=14, 
          color="#B823EA", weight='bold')
plt.xlabel('Meses')
plt.ylabel('Vendas (R$)')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()