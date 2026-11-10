import matplotlib.pyplot as plt

# Dados de exemplo
setores = ['Marketing', 'Vendas', 'TI', 'RH', 'Financeiro']
percentuais = [20, 25, 30, 15, 10]

# Criando o gráfico de pizza
cores = ['#8E4585', "#FFFF00", "#FF0000",
         "#FA8E60", '#6F2DA8']
plt.figure(figsize=(6,6))
plt.pie(percentuais, labels=setores, autopct='%1.1f%%',
        startangle=90, colors=cores, pctdistance=0.75,
        textprops={'fontsize': 11, 'weight': 'bold'})
plt.title('Distribuição de Orçamento por Setor',
          fontsize=16, color='#6F2DA8', weight='bold')
plt.axis('equal')  # Garante que o gráfico seja um círculo
plt.tight_layout()
plt.show()
