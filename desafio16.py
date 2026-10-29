comentario = input("Digite o comentário do cliente sobre o produto: ")
comentario_tratado = comentario.lower()
print("\n--- Analizador de Feedback ---")
if "defeito" in comentario_tratado or "quebrou" in comentario_tratado or "ruim" in comentario_tratado:
   print("Alerta Crítico: Feedback negativo detectado! Encaminhar para o suporte técnico")
else:
   print("Feedback Normal: Comentários sem alertas de falhas críticas.")