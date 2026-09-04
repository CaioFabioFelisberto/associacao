from apyori import apriori

# Simulando um log de playlists (o que a galera escuta junto na mesma sessão)
playlists = [
    ["Metallica", "Black Sabbath", "Iron Maiden"],
    ["Bathory", "Mayhem", "Darkthrone"],
    ["Metallica", "Black Sabbath", "Bathory"],
    ["Black Sabbath", "Dio", "Judas Priest"],
    ["Metallica", "Black Sabbath", "Megadeth"],
    ["Bathory", "Darkthrone", "Mayhem"],
    ["Iron Maiden","Judas Priest", "Diamond Head"],
    ["Anthrax","Metallica","Slayer"],
    ["Iron Maiden","Black Sabbath","Jethro Tull"],
    ["Jethro Tull",'Iron Maiden', 'Black Sabbath'],
    ['Metallica', 'Iron Maiden', 'Black Sabbath'],
    ['Iron Maiden','Bathory','Jethro Tull']
]

print("🎸 Minerando os padrões musicais...\n")

# Rodando o algoritmo
# min_support = 0.2 (o conjunto tem que aparecer em pelo menos 20% das playlists, ou seja, 1 de 5)
regras_geradas = apriori(playlists, min_support=0.2, min_confidence=0.7, min_lift=1.0)

# O apyori retorna um "generator" em Python. A gente converte pra lista pra conseguir iterar e ler os dados.
resultados = list(regras_geradas)

# Aqui é onde a mágica acontece. Vamos destrinchar o objeto RelationRecord.
for regra in resultados:
    # A variável 'regra' é uma tupla. 
    # regra[0] = frozenset com os itens da regra (ex: Metallica, Black Sabbath)
    # regra[1] = suporte total desse conjunto
    # regra[2] = lista de objetos OrderedStatistic (que contém a direção da regra, confiança e lift)
    
    suporte = regra[1]
    
    # Podemos ter várias direções para os mesmos itens (A -> B ou B -> A), por isso iteramos de novo
    for estatistica in regra[2]:
        # estatistica[0] = antecedente (quem engatilha a regra - a base)
        # estatistica[1] = consequente (o que é recomendado)
        antecedente = list(estatistica[0])
        consequente = list(estatistica[1])
        confianca = estatistica[2]
        lift = estatistica[3]
        
        # O apyori às vezes gera regras "vazias" apontando pra um item. A gente filtra isso.
        if len(antecedente) > 0:
            # Transformando as listas em strings mais bonitas pra printar
            str_antecedente = ", ".join(antecedente)
            str_consequente = ", ".join(consequente)
            
            print(f"🔥 Se o cara escuta: [{str_antecedente}]")
            print(f"👉 Logo vai escutar: [{str_consequente}]")
            print(f"   🔹 Suporte:   {suporte:.2f} ({suporte*100:.0f}% das playlists globais)")
            print(f"   🔹 Confiança: {confianca:.2f} ({confianca*100:.0f}% de chance)")
            print(f"   🔹 Lift:      {lift:.2f}")
            print("-" * 50)