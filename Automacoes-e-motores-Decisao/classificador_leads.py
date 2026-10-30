nome_da_empresa = input("Digite o nome da empresa: ")
setor_atuacao = input("Digite o seguimento de atuação da empresa: ")
quantidade_funcionarios = int(input("Digite a quantidade de funcionários da empresa: "))
faturamento_estimado = float(input("Digite o faturamento mensal da empresa: "))

if quantidade_funcionarios >= 500:
    pontos_volume = 40
elif quantidade_funcionarios >= 100:
    pontos_volume = 20
else:
    pontos_volume = 5
if faturamento_estimado >= 1000000:
    pontos_faturamento = 40
elif faturamento_estimado >= 200000:
    pontos_faturamento = 20
else:
    pontos_faturamento = 5
setor_atuacao = setor_atuacao.strip().lower()
if setor_atuacao in ["técnologia", "tecnologia", "saude", "saúde"]:
    pontos_bonus = 20
else:
    pontos_bonus = 0
pontos_finais = pontos_volume + pontos_faturamento + pontos_bonus
print(f"A empresa {nome_da_empresa} Obteve a pontuação final de  : {pontos_finais}")
if pontos_finais >= 80:
    print("Lead de Alta Prioridade! Roteando imediatamente para a equipe de Enterprise Sales.")
elif pontos_finais >= 50:
    print("Lead de Média Prioridade. Roteando para a equipe de Inside Sales.")
else:
    print("Lead de baixa prioridade. Roteando para a equipe de inside sales. Lead será analisado e guardado em nosso banco de dados para futuras oportunidades.")
