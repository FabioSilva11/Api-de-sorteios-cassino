# API de Sorteio

A API de Sorteio é uma aplicação simples desenvolvida em Flask que permite a integração de sorteios de símbolos em outros projetos. Ela é especialmente útil para casos em que é necessário incluir elementos de sorteio, como em jogos ou aplicações interativas.

## Funcionalidades

- **Realização de Sorteios**: A API realiza sorteios aleatórios de símbolos a cada requisição.
- **Variedade de Símbolos**: Diversos símbolos estão disponíveis, cada um associado a um valor e a uma URL de imagem.
- **Personalização de Resultados**: A cada 1000 requisições, a API retorna três símbolos idênticos, proporcionando uma experiência mais dinâmica.

## Uso em Projetos

A API pode ser integrada facilmente em projetos Python ou em outras aplicações web. Aqui estão os passos básicos para utilização:

1. **Instalação das Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Execução da API**:
   ```bash
   python app.py
   ```

   A API estará disponível em http://127.0.0.1:5000/.

3. **Integração em Projetos Python**:
   - Importe o módulo `requests` para realizar requisições à API.
   - Exemplo de uso em Python:
     ```python
     import requests

     # Exemplo de requisição à API
     response = requests.get("http://127.0.0.1:5000/resultado_sorteio")
     resultado_sorteio = response.json()

     print("Resultado do Sorteio:", resultado_sorteio)
     ```

4. **Integração em Projetos Web**:
   - Utilize bibliotecas ou frameworks web para fazer requisições à API a partir do lado do cliente (por exemplo, JavaScript com Fetch API ou jQuery).

## Rotas

- **/resultado_sorteio**: Retorna o resultado do sorteio em formato JSON.
- **/**: Rota padrão que exibe uma mensagem indicando que a API está no ar.

A API de Sorteio proporciona uma maneira fácil e flexível de incluir sorteios em projetos, adicionando um elemento interativo e surpreendente para os usuários.
```
