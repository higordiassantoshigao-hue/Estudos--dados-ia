faturamento_total = 0
continuar_lancando = True

while continuar_lancando == True:
    valor_venda = int(input("Digite o valor da venda (ou 0 para encerrar o dia): "))

    if valor_venda == 0:
        print("Encerrando os lancamentos do caixa...")
        continuar_lancando = False
    else:
        faturamento_total = faturamento_total + valor_venda
        print("Venda computada! Faturamento total acumulado: R$", faturamento_total)

print("___ Fechamento de caixa dos dados ___")
print("O fatuturamento total do dia foi: R$", faturamento_total)