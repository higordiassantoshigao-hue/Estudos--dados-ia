baseline = 500.0
peso_pecas = [502.5, 498.0, 505.0, 501.0, 499.5, 500.5, 500.8, 499.2]
for peso in peso_pecas:
    diferenca_percentual = (abs(peso - baseline) / baseline) * 100
    print(f"Peso da peça: {peso:.1f}g | Desvio: {diferenca_percentual:.2f}%")
    if diferenca_percentual > 2.0:
        print(f"Alerta: Peça com peso {peso:.1f}g ultrapassou o limite com {diferenca_percentual:.2f}% de desvio!")
    else:
        print(" ✅ Peça aprovada com sucesso! Produção dentro do limite de 2% de desvio.")
