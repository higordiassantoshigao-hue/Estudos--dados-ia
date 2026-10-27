score_de_crédito = int(input("Digite o score do cliente: "))
if score_de_crédito < 300:
 print("Perfil de alto risco. Crédito negado.")
elif score_de_crédito <= 699:
 print("Perfil moderado.Liberar cartão basico com limite de R$500.00.")
else:
 print("Perfil exelente! Liberar cartão vip com limite black.")