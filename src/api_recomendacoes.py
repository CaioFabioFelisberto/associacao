from flask import Flask, request, jsonify
from apyori import apriori

app = Flask(__name__)

# Simulação de dados (num ambiente de prod, puxaríamos isso de uma query cabulosa no SQL ou de um cluster)
transacoes = [
    ["AK-47 Redline", "AWP Asiimov", "Glove Case"],
    ["AK-47 Redline", "M4A4 Neo-Noir"],
    ["AWP Asiimov", "Glove Case", "Desert Eagle Printstream"],
    ["AK-47 Redline", "AWP Asiimov", "Glove Case", "Desert Eagle Printstream"],
    ["M4A4 Neo-Noir", "Desert Eagle Printstream", "Glove Case"],
    ["AK-47 Redline", "Glove Case", "M4A4 Neo-Noir"]
]

print("⚙️ Minerando as regras de associação na inicialização do server...")
# Rodando o algoritmo da biblioteca apyori
# Ajuste fino: suporte mínimo, confiança e lift para evitar recomendar lixo
regras_brutas = apriori(transacoes, min_support=0.3, min_confidence=0.5, min_lift=1.1)

# Dicionário em memória para o lookup da API ser O(1) na hora da requisição
motor_recomendacao = {}

for regra in regras_brutas:
    pares = regra[2] # ordered_statistics da lib
    for par in pares:
        antecedente = list(par[0])
        consequente = list(par[1])
        lift = par[3]
        
        # Filtrando regras simples de 1 para 1 para a nossa API
        if len(antecedente) == 1 and len(consequente) == 1:
            item_base = antecedente[0]
            item_rec = consequente[0]
            
            if item_base not in motor_recomendacao:
                motor_recomendacao[item_base] = []
            
            motor_recomendacao[item_base].append({
                "item_recomendado": item_rec,
                "forca_lift": round(lift, 2)
            })

# Ordenando as recomendações pelo maior Lift (o que mais converte em vendas primeiro)
for item in motor_recomendacao:
    motor_recomendacao[item] = sorted(motor_recomendacao[item], key=lambda x: x['forca_lift'], reverse=True)

print("✅ IA pronta pra rodar!")

# Rota principal da nossa API
@app.route('/recommend', methods=['GET'])
def recomendar():
    # Pegando o item da URL. Ex: /recommend?item=AWP Asiimov
    item_comprado = request.args.get('item')
    
    if not item_comprado:
        return jsonify({"erro": "Faltou o parâmetro, parça! Manda um ?item=NomeDoItem na URL."}), 400
        
    recomendacoes = motor_recomendacao.get(item_comprado, [])
    
    if recomendacoes:
        return jsonify({
            "mensagem": f"Opa! Quem leva {item_comprado} costuma levar também:",
            "data": recomendacoes
        }), 200
    else:
        return jsonify({
            "mensagem": "Sem dados suficientes pra associar algo a esse item.",
            "data": []
        }), 404

if __name__ == '__main__':
    # Rodando o server na porta 5000
    app.run(debug=True, port=5000)