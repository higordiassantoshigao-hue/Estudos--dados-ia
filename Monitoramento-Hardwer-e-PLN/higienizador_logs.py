log_bruto ="---  ALERTA: Erro crítico no ModuLo_IA... falha de conexão com o banco De dados!!!  "
log_limpo = log_bruto .strip() .lower() .replace('!!!',  '') .replace('---', '')
total_erros = log_limpo.count("erro")
total_falhas = log_limpo.count("falha")
print(f"log_bruto: '{log_bruto}'")
print(f"log_limpo: '{log_limpo}'")
print(f"Total de erros: {total_erros}")
print(f"Total de falhas: {total_falhas}")
