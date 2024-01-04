import random
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Dicionário de opções de imagens com URLs
opcoes = {
    "cereja": {"valor": 5, "img": "https://minha-imagem/cereja.png"},
    "limao": {"valor": 8, "img": "https://minha-imagem/limao.png"},
    "laranja": {"valor": 3, "img": "https://minha-imagem/laranja.png"},
    "uva": {"valor": 7, "img": "https://minha-imagem/uva.png"},
    "7": {"valor": 10, "img": "https://minha-imagem/sete.png"}
}

# Contador para controlar as requisições
contador_requisicoes = 0

# Função para realizar um sorteio
def realizar_sorteio():
    global contador_requisicoes
    contador_requisicoes += 1

    # A cada 1000 requisições, mostrar três símbolos idênticos
    if contador_requisicoes % 1000 == 0:
        simbolo = random.choice(list(opcoes.keys()))
        sorteios = [opcoes[simbolo].copy() for _ in range(3)]
    else:
        # Caso contrário, retorna 3 símbolos diferentes
        simbolos_aleatorios = random.sample(list(opcoes.keys()), 3)
        sorteios = [opcoes[simbolo].copy() for simbolo in simbolos_aleatorios]

    return sorteios

# Rota para retornar o resultado dos sorteios
@app.route('/resultado_sorteio', methods=['GET'])
def obter_resultado_sorteio():
    resultados_combinados = realizar_sorteio()
    return jsonify(resultados_combinados)

# Rota padrão
@app.route('/')
def homepage():
    return "A API está no ar"

# Rodar a nossa API
if __name__ == '__main__':
    app.run(host='0.0.0.0')
