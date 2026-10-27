temperatura = int(input("Digite a temperatura atual: "))
if temperatura <=0:
 print("Alerta: Temperatura congelante! Risco de falha no sistema.")
elif temperatura <=70:
 print("Temperatura normal. Operando com segurança.")
if temperatura >=70:
 print("Alerta Crítico: Superaquecimento! Desligando módulus de IA.") 