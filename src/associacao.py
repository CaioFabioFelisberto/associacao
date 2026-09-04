# Nosso "banco de dados" em formato JSON/Lista
# Cada lista interna é uma transação (carrinho de compras de um usuário)
transacoes = [
    ["AK-47 Redline", "AWP Asiimov", "Glove Case"],
    ["AK-47 Redline", "M4A4 Neo-Noir"],
    ["AWP Asiimov", "Glove Case", "Desert Eagle Printstream"],
    ["AK-47 Redline", "AWP Asiimov", "Glove Case", "Desert Eagle Printstream"],
    ["M4A4 Neo-Noir", "Desert Eagle Printstream"]
]

total_transacoes = len(transacoes)

# 1. SUPORTE: Qual a frequência que um conjunto de itens aparece no total?
def calcular_suporte(itemset, transacoes):
    # Conta quantas vezes o itemset completo aparece nas transações
    contagem = sum(1 for t in transacoes if set(itemset).issubset(set(t)))
    return contagem / total_transacoes

# 2. CONFIANÇA: Se o cara comprou A, qual a chance de comprar B?
# Fórmula: Suporte(A e B) / Suporte(A)
def calcular_confianca(item_A, item_B, transacoes):
    suporte_A = calcular_suporte(item_A, transacoes)
    suporte_A_B = calcular_suporte(item_A + item_B, transacoes) # União dos itens
    
    if suporte_A == 0:
        return 0
    return suporte_A_B / suporte_A

# 3. LIFT: O quão mais provável é comprar B tendo comprado A, em relação a comprar B do nada?
# Fórmula: Confiança(A -> B) / Suporte(B)
# Se Lift > 1, tem associação forte (um puxa o outro). Se < 1, eles se repelem.
def calcular_lift(item_A, item_B, transacoes):
    confianca_A_B = calcular_confianca(item_A, item_B, transacoes)
    suporte_B = calcular_suporte(item_B, transacoes)
    
    if suporte_B == 0:
        return 0
    return confianca_A_B / suporte_B

# --- Testando a nossa IA caseira ---

# Queremos descobrir a regra: "Quem compra 'AK-47 Redline' (A) também compra 'Desert Eagle Printstream' (B)?"
item_A = ["AK-47 Redline"]
item_B = ["Desert Eagle Printstream"]

sup = calcular_suporte(item_A + item_B, transacoes)
conf = calcular_confianca(item_A, item_B, transacoes)
lift = calcular_lift(item_A, item_B, transacoes)

print(f"📊 Analisando a Regra: {item_A} -> {item_B}")
print(f"🔹 Suporte (A e B juntos): {sup * 100:.2f}% das transações")
print(f"🔹 Confiança (Se A, então B): {conf * 100:.2f}% de chance")
print(f"🔹 Lift (Força da regra): {lift:.2f}")

if lift > 1:
    print("🔥 Veredito: Associação braba! Vale a pena recomendar um quando o cara comprar o outro.")
else:
    print("🧊 Veredito: Associação fraca. Melhor não gastar processamento recomendando isso junto.")