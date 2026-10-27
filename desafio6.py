quantidade_de_cliques = int(input("Digite o número de cliques de hoje: "))
if quantidade_de_cliques < 100:
 print("Campanha Fria: Dessempenho abaixo do esperado. Sugerir troca de criativo.")
elif quantidade_de_cliques <= 500:
 print("Campanha Estável: Engajamento dentro da média.")
else:
 print("Campanha Quente! Sucesso absoluto. Recomendar aumento de orçamento.")