# Passo 1: Entrada das notas de avaliação (de 0 a 10)
nota_qualidade = float(input("Digite a nota de qualidade (0 a 10): "))
nota_preco = float(input("Digite a nota de preço (0 a 10): "))

# Passo 2: Definição dos pesos das métricas
peso_qualidade = 7
peso_preco = 3

# Passo 3: Cálculo da Média Ponderada
soma_pesos = peso_qualidade + peso_preco
media_ponderada = ((nota_qualidade * peso_qualidade) + (nota_preco * peso_preco)) / soma_pesos

# Passo 4: Relatório final de performance
print("\n--- AVALIAÇÃO FINAL DO FORNECEDOR ---")
print(f"Média Ponderada de Performance: {media_ponderada:.1f}")

if media_ponderada >= 7.0:
    print("🤝 Fornecedor Aprovado! Manter contrato ativo.")
else:
    print("⚠️ Fornecedor em Alerta! Performance abaixo do esperado.")
