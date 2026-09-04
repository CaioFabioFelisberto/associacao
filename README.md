# 📊 Mineração de Regras de Associação - Projeto Educacional

Um projeto de estudos e testes sobre **Associação de Itens** (Market Basket Analysis) usando Python. Implementa algoritmos clássicos como **Apriori** e **ECLAT** para descobrir padrões de compra e gerar recomendações baseadas em dados transacionais.

## 🎯 O Que É Mineração de Regras de Associação?

É uma técnica de Data Mining que encontra padrões em dados transacionais. Responde perguntas como:

> "Se um cliente compra AK-47 Redline, qual a probabilidade dele também comprar Desert Eagle Printstream?"

### Conceitos Principais

- **Suporte (Support)**: Frequência que um conjunto de itens aparece no total de transações
  ```
  Suporte(A) = (Transações com A) / (Total de Transações)
  ```

- **Confiança (Confidence)**: Probabilidade de B ser comprado dado que A foi comprado
  ```
  Confiança(A → B) = Suporte(A ∩ B) / Suporte(A)
  ```

- **Lift**: Força da associação entre itens. Indica se A e B se correlacionam
  ```
  Lift(A → B) = Confiança(A → B) / Suporte(B)
  ```
  - Lift > 1: Forte associação (um puxa o outro)
  - Lift = 1: Sem associação
  - Lift < 1: Negativa (se um vende, o outro não vende)

## 🗂️ Estrutura do Projeto

```
associacao/
├── src/
│   ├── associacao.py           # Implementação manual de Support, Confidence e Lift
│   ├── apyori_test.py          # Teste com biblioteca Apyori (análise de playlists)
│   ├── api_recomendacoes.py    # API Flask com motor de recomendação
│   └── teste_eclat.py          # Teste com algoritmo ECLAT
├── requirements.txt            # Dependências do projeto
├── .gitignore                  # Arquivo de gitignore
└── README.md                   # Este arquivo
```

## 📦 Dependências

O projeto utiliza as seguintes bibliotecas:

- **apyori** (1.1.2): Implementação do algoritmo Apriori
- **pyECLAT** (1.0.2): Implementação do algoritmo ECLAT
- **Flask** (3.1.3): Framework web para a API
- **NumPy** (2.5.2): Operações numéricas
- **Pandas** (3.0.5): Análise de dados
- **tqdm** (4.70.0): Barras de progresso

Ver [requirements.txt](requirements.txt) para a lista completa.

## ⚙️ Instalação

### Pré-requisitos
- Python 3.8+

### Passos

1. **Clone ou acesse o repositório:**
   ```bash
   cd associacao
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv .venv
   ```

3. **Ative o ambiente virtual:**
   - **Windows:**
     ```bash
     .\.venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source .venv/bin/activate
     ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Como Usar

### 1. Teste Básico - Implementação Manual

Entenda os conceitos fundamentais com cálculos manuais:

```bash
python src/associacao.py
```

**Exemplo de saída:**
```
📊 Analisando a Regra: ['AK-47 Redline'] -> ['Desert Eagle Printstream']
Suporte: 0.40
Confiança: 0.67
Lift: 1.67
```

### 2. Teste com Apyori - Análise de Playlists

Descobre padrões de audição de bandas em playlists:

```bash
python src/apyori_test.py
```

**Exemplo de saída:**
```
🎸 Minerando os padrões musicais...

Se ouve: Metallica → Também ouve: Black Sabbath
  Suporte: 0.33 | Confiança: 0.80 | Lift: 1.45
```

### 3. Teste com ECLAT

Algoritmo alternativo para mineração (vertical itemset):

```bash
python src/teste_eclat.py
```

### 4. API REST de Recomendações

Inicie o servidor Flask:

```bash
python src/api_recomendacoes.py
```

A API estará disponível em `http://localhost:5000`

#### Endpoints

**GET `/recomendacoes/<item>`**

Retorna itens recomendados baseado em padrões de compra.

```bash
curl http://localhost:5000/recomendacoes/AK-47%20Redline
```

**Resposta:**
```json
{
  "item_solicitado": "AK-47 Redline",
  "recomendacoes": [
    {
      "item": "Desert Eagle Printstream",
      "lift": 1.67
    },
    {
      "item": "AWP Asiimov",
      "lift": 1.40
    }
  ]
}
```

**GET `/dados`**

Retorna as transações analisadas:

```bash
curl http://localhost:5000/dados
```

## 📚 Casos de Uso

Este projeto ilustra aplicações reais de mineração de associação:

- **E-commerce**: "Clientes que compram X também compram Y"
- **Streaming**: "Usuários que escutam Banda A também escutam Banda B"
- **Supermercados**: "Clientes que compram fraldas também compram cerveja"
- **Recomendação de Produtos**: Sistemas de sugestão cross-sell

## 🔬 Parametrização do Algoritmo

Nos scripts, você pode ajustar os limiares de mineração:

```python
apriori(
    transacoes,
    min_support=0.3,      # Mínimo 30% de frequência
    min_confidence=0.5,   # Mínimo 50% de confiança
    min_lift=1.1          # Mínimo lift de 1.1
)
```

- **Aumentar `min_support`**: Encontra padrões mais frequentes (menos ruído)
- **Aumentar `min_confidence`**: Regras mais "seguras"
- **Aumentar `min_lift`**: Associações mais fortes

## 🧪 Testando com Seus Dados

Substitua as transações nos scripts pelas suas:

```python
transacoes = [
    ["item_1", "item_2", "item_3"],
    ["item_1", "item_4"],
    # ... mais transações
]
```

## 📖 Documentação de Referência

- **Apyori**: https://github.com/yu-qi/Apyori
- **PyECLAT**: https://github.com/zzzzz0/Py-ECLAT
- **Algoritmo Apriori**: https://en.wikipedia.org/wiki/Apriori_algorithm
- **ECLAT**: https://en.wikipedia.org/wiki/Association_rule_learning#Eclat

## 💡 Dicas de Aprendizado

1. **Comece pela `associacao.py`**: Entenda os conceitos manualmente
2. **Experimente com `apyori_test.py`**: Use a biblioteca para casos reais
3. **Ajuste os parâmetros**: Veja como mudam os resultados
4. **Implemente na API**: Use os padrões em uma aplicação web

## ⚠️ Limitações

- Os dados são em memória (não ideal para datasets gigantes)
- Transações ficam em lista Python (use SQL para produção)
- API não tem autenticação (projeto educacional)

## 🔧 Próximas Melhorias

- [ ] Integração com banco de dados (SQLite, PostgreSQL)
- [ ] Cache para resultados de mineração
- [ ] Dashboard com visualizações (Matplotlib, Plotly)
- [ ] Testes unitários
- [ ] Deploy em Docker
- [ ] Análise incremental (dados em stream)

## 📝 Licença

Projeto educacional - Livre para uso em estudos.

## 👤 Autor

Desenvolvido como projeto de estudos em Data Mining e Machine Learning.

---

**Happy Mining! 🎸📊**

