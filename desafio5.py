import time
import random

print("--- Sistema de Monitoramento Contínuo de Hardware de IA ---")
historico_temperaturas = []
temperatura_anterior = None
tempo_anterior = None
LIMITE_CRITICO = 70

while True:
    temperatura_atual = random.randint(55, 75)
    tempo_atual = time.time()

    print(f"\n[Monitor] Temperatura atual do chip de IA: {temperatura_atual}°C")

    historico_temperaturas.append(temperatura_atual)
    if len(historico_temperaturas) > 5:
        historico_temperaturas.pop(0)

    media_movel = sum(historico_temperaturas) / len(historico_temperaturas)
    print(f"-> [Estatistica] Média móvel atual: {media_movel:.1f}°C")

    if temperatura_anterior is not None and tempo_anterior is not None:
        dt = tempo_atual - tempo_anterior
        dT = temperatura_atual - temperatura_anterior
        taxa_variacao = dT / dt

        print(f"-> [Cálculo] Taxa de variação (dT/dt): {taxa_variacao:+.2f}°C/s")
        if taxa_variacao > 5:
            print("Alerta de Derivada: Pico de calor extremo detectado! Taxa de variação perigosa.")

    if temperatura_atual <= 0:
        print("Alerta: Temperatura congelante! Risco de falha no sistema.")
    elif temperatura_atual < LIMITE_CRITICO:
        print("Temperatura normal. Operando com segurança")
    else:
        print("Alerta Crítico! Superaquecimento do sistema! Desligando módulos de IA para proteção.")
        break

    temperatura_anterior = temperatura_atual
    tempo_anterior = tempo_atual
    time.sleep(2)


