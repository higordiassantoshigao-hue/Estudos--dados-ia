nome_do_candidato = input("Digite o seu nome: ")
nota_do_teste = int(input("N: "))
tempo_de_experiencia = int(input("Digite seu tempo de experiência na áerea: "))
pretensao_salarial = int(input("Digite sua pretensão Salarial: "))
if nota_do_teste >= 70:
    pontos_atuais = 50
elif nota_do_teste >= 40:
    pontos_atuais =  30 
else:
    pontos_atuais = 5
if tempo_de_experiencia <= 1:
    pontos_experiencia = 10
elif tempo_de_experiencia <= 3:
    pontos_experiencia = 20
else: 
    pontos_experiencia =  30
if pretensao_salarial >= 5000:
    pontos_salarial = 10
elif pretensao_salarial <= 5000:
    pontos_salarial = 30
else:
    pontos_salarial = 0 
pontos_finais = pontos_atuais + pontos_experiencia + pontos_salarial    
print(f"O candidato {nome_do_candidato} obteve a pontuação final de: {pontos_finais}")
if pontos_finais >= 80:
    print("O Candidato foi aprovado para a próxima fase do processo seletivo.")
elif pontos_finais >= 49:
    print("O Candidato foi enviado para a lista de espera para as próximas fases de processo seletivo. Seu dados serão analizados e guardados em nosso banco de dados para futuras oportunidades.")
else:
   print("O candidato não atingiu a pontuação mínima para aprovação. Infelizmente, não será possível avançar para a próxima fase do processo seletivo.")