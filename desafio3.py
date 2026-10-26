pontos_atuais= int(input("Digite a pontuação atual do cliente: "))
meses_ativo= int(input("Digite quantos meses o cliente está ativo: "))
if meses_ativo <=6:
 bônus = pontos_atuais * 0.05
 print("Cliente Recente. bônus de 5%.")
elif meses_ativo <=12:
 bônus = pontos_atuais * 0.10
 print("Cliente Intermediário. Bônus de 10%.")
else:
 bônus = pontos_atuais * 0.20
 print("Cliente Vip! Bônusd de 20%.")
pontos_finais = pontos_atuais + bônus
print(f"O valor do bônus é: {bônus}")
print(f"A pontuação final do Cliente é: {pontos_finais}")