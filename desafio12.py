faturamento_mês_passado = float(input("Digite o faturamento do mês anterior: R$ "))
Faturamento_mês_atual = float(input("Digite o faturamento do mês atual: R$ "))
Variação_absoluta = faturamento_mês_passado - Faturamento_mês_atual
crescimento_percentual = (Variação_absoluta / faturamento_mês_passado) * 100

print("\n--- Análise De Crescimento ---")
print(f"Variação De Faturamento: R$ {Variação_absoluta:.2f}")
print(f"Taxa De Crescimento: {crescimento_percentual:.2f}%")
if crescimento_percentual > 0:
    print("Resultado Positivo! O Negócio Está Em Expansão")
elif crescimento_percentual < 0:
    print("Alerta De Queda! O Faturamento Encolheu Em relação ao mês passado.") 
else:
    print("Estabilidade Completa. O faturamento se Manteve Idêntico.")
