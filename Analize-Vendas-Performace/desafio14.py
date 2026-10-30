media_referencia = 1000.0

# Passo 2: Recebemos a produção do dia atual
producao_hoje = float(input("Digite a quantidade de peças produzidas hoje: "))

# Passo 3: Calculamos a variação em relação à referência
diferenca_percentual = ((producao_hoje - media_referencia) / media_referencia) * 100

# Passo 4: Checagem de dispersão (Alerta se passar de 20% ou -20%)
print("\n--- ANÁLISE DE DISPERSÃO DA PRODUÇÃO ---")
print(f"Desvio calculado: {diferenca_percentual:.1f}%")

if diferenca_percentual > 20.0:
    print("🔥 Alerta Crítico: Produção muito acima da média! Risco de sobrecarga nas máquinas.")
elif diferenca_percentual < -20.0:
    print("🚨 Alerta Crítico: Produção muito abaixo da média! Investigar ócio ou quebra de maquinário.")
else:
    print("✅ Produção Estável: Dentro da margem de segurança de 20%.")
