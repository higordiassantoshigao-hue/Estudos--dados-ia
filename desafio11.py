vendas_semana = [1500, 2300, 950, 4100, 1200, 2300, 3100]

total_faturado = sum(vendas_semana)
quantidade_vendas = len(vendas_semana)
média_vendas = total_faturado / quantidade_vendas
pior_dia = min(vendas_semana)
melhor_dia = max(vendas_semana)
amplitude = melhor_dia - pior_dia
print("---Relatório Estatístico de vendas---")
print("Faturamento total: R$", total_faturado)
print("Quantidade de dias analizados:", pior_dia)
print(f"Média diária de vendas: R$ {média_vendas:.2f}")
print("Pior dia de vendas (mínimo): R$", pior_dia)
print("Melhor dia de vendas (máximo): R$", melhor_dia)
print("Amplitude de dispersão (máx - mín): R$", amplitude)