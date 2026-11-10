import matplotlib.pyplot as plt

# Dados de exemplo
produtos = ['Ameixa', 'Banana','Maça', 'Laranja', 'Uva', 'Kiwi']
vendas = [120, 210, 160, 260, 190,230]

# Criando o gráfico de barras
cores = ['#8E4585', "#FFFF00", "#FF0000",
         "#FA8E60", '#6F2DA8','#92EA43']
plt.bar(produtos, vendas, color=cores)
plt.title('Vendas por Produto', fontsize=14,
          color='#6F2DA8', weight='bold')
plt.xlabel('Produtos', fontsize=11)
plt.ylabel('Vendas (R$)', fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

