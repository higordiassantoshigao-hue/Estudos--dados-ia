quantidade = int(input("Digite o número de funcionários da empresa: "))
if quantidade < 10:
 print("Empresa pequena: Enviar para a afilial de atendimento automatizado.")
elif quantidade <= 100:
 print("Empresa média: Enviar para equipe de vendas internas.")
else:
 print("Empresa grande Vip! Chamar um gerente de contas imediatamente.")