import requests

# URL oficial da API de testes (verifique se não há espaços antes ou depois)
url = url = "https://api.restful-api.dev/objects"  # Substitua pela URL real da API

print(f"Enviando requisição para: {url}...")
resposta = requests.get(url)

print(f"Status da Resposta: {resposta.status_code}")

# Boa prática de Engenharia de Dados: Só processa se o status for 200 (Sucesso)
if resposta.status_code == 200:
    dados_produtos = resposta.json()
    precos_encontrados = []

    for produtos in dados_produtos:
        if "data" in produtos and produtos["data"] is not None:
            if "price" in produtos["data"]:
                preco = produtos["data"]["price"]
                
                if "apple" in produtos["name"].lower():
                    print(f"🍏 Produto Apple Encontrado: {produtos['name']} | Preço: ${preco}")
                    precos_encontrados.append(preco)

    print("\n--- Relatório de Extração Web ---")
    print("Quantidade de preços coletados com sucesso:", len(precos_encontrados))

    if len(precos_encontrados) > 0:
        media_precos = sum(precos_encontrados) / len(precos_encontrados)
        print(f"Média de preços dos produtos Apple: ${media_precos:.2f}")
    else:
        print("Nenhum produto Apple com preço foi encontrado.")

else:
    print("\n🚨 Erro na Coleta!")
    print(f"O servidor retornou o status {resposta.status_code} em vez de 200.")
    print("Verifique se a URL foi digitada corretamente ou tente novamente mais tarde.")


