import pandas as pd
from pyECLAT import ECLAT

# O nosso dataset brabo de metal, já com o "Maiden" corrigido pra não zoar a matemática
playlists = [
    ["Metallica", "Black Sabbath", "Iron Maiden"],
    ["Bathory", "Mayhem", "Darkthrone"],
    ["Metallica", "Black Sabbath", "Bathory"],
    ["Black Sabbath", "Dio", "Judas Priest"],
    ["Metallica", "Black Sabbath", "Megadeth"],
    ["Bathory", "Darkthrone", "Mayhem"],
    ["Iron Maiden", "Judas Priest", "Diamond Head"],
    ["Anthrax", "Metallica", "Slayer"],
    ["Iron Maiden", "Black Sabbath", "Jethro Tull"],
    ["Jethro Tull", "Iron Maiden", "Black Sabbath"],
    ["Metallica", "Iron Maiden", "Black Sabbath"]
]

print("🎸 Carregando os dados pro Pandas...")
# O pyECLAT precisa que cada transação seja uma linha no DataFrame
df = pd.DataFrame(playlists)

# Mostrando como o DataFrame fica (ele preenche com NaN onde não tem banda na coluna)
print(df.head())
print("-" * 50)

print("⚡ Rodando o motor do ECLAT...\n")
# Instanciando a classe passando o DataFrame
motor_eclat = ECLAT(data=df, verbose=True)

# Executando o algoritmo
# min_support = 0.2 (Aparecer em pelo menos 20% das playlists)
# min_combination = 2 (Queremos no mínimo pares, nada de banda sozinha)
# max_combination = 3 (Até trincas de bandas pra não explodir a memória se a base for gigante)
indices, suportes = motor_eclat.fit(min_support=0.2, min_combination=2, max_combination=3)

# O pyECLAT retorna dois dicionários: 
# 1. 'indices' tem os IDs das linhas onde o padrão apareceu (a abordagem vertical em ação)
# 2. 'suportes' tem o valor percentual da frequência

# Vamos printar os resultados de um jeito limpo
print("\n🔥 Padrões Frequentes Encontrados:\n")
for itemset, suporte_valor in suportes.items():
    # O pyECLAT junta os itens com um '&' (ex: Metallica & Black Sabbath)
    bandas = itemset.replace(" & ", " + ")
    pct = suporte_valor * 100
    
    print(f"🤘 {bandas}")
    print(f"   🔹 Suporte: {suporte_valor:.2f} ({pct:.0f}% das playlists)")
    print("-" * 40)