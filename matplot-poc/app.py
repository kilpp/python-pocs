import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt

# Configuração dos Dados
labels_perfil = ['Clientes (187)', 'Equipe/Fornecedores (25)']
tamanhos_perfil = [187, 25]
cores_perfil = ['#4CAF50', '#FFC107'] # Verde e Amarelo

# Dados Improvisados para a Questão de Acessibilidade (Barreira)
barreiras = ['Escadas/Falta de Rampa', 'Banheiro Inadequado', 'Circulação Interna', 'Nenhuma']
votos_barreiras = [130, 50, 22, 10] # Improvised numbers summing to 212

# Dados sobre Apoio à Melhoria (Conclusão)
labels_apoio = ['A Favor da Inclusão/Reforma', 'Satisfeitos com Atual']
tamanhos_apoio = [203, 9] # 96% a favor
cores_apoio = ['#2196F3', '#E0E0E0'] # Azul destaque e Cinza

# --- PLOT 1: Perfil dos Respondentes (Pizza) ---
plt.figure(figsize=(8, 6))
plt.pie(tamanhos_perfil, labels=labels_perfil, autopct='%1.1f%%', startangle=140, colors=cores_perfil)
plt.title('Perfil dos Respondentes (Total: 212)')
plt.axis('equal') 
plt.savefig('perfil_respondentes.png', dpi=300, bbox_inches='tight')
print('Saved: perfil_respondentes.png')
plt.close()

# --- PLOT 2: Principais Barreiras Identificadas (Barras) ---
plt.figure(figsize=(10, 6))
plt.bar(barreiras, votos_barreiras, color='#FF5722')
plt.title('Maior Dificuldade Encontrada (Infraestrutura)')
plt.xlabel('Barreira Citada')
plt.ylabel('Número de Pessoas')
plt.grid(axis='y', alpha=0.3)
plt.savefig('barreiras_identificadas.png', dpi=300, bbox_inches='tight')
print('Saved: barreiras_identificadas.png')
plt.close()

# --- PLOT 3: Consenso sobre Melhoria (Pizza) ---
plt.figure(figsize=(8, 6))
plt.pie(tamanhos_apoio, labels=labels_apoio, autopct='%1.1f%%', startangle=90, colors=cores_apoio, explode=(0.1, 0))
plt.title('Consenso: Apoio ao Projeto de Acessibilidade')
plt.axis('equal')
plt.savefig('consenso_apoio.png', dpi=300, bbox_inches='tight')
print('Saved: consenso_apoio.png')
plt.close()