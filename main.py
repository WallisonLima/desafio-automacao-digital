# Sistema simples de controle de qualidade

# Critérios de aprovação:
# - Peso entre 95 e 105
# - Cor: azul ou verde
# - Comprimento entre 10 e 20
# - 10 peças por caixa

pecas_aprovadas = []
pecas_reprovadas = []
caixas = []
caixa_atual = []

while True:
    print("\n--- Cadastro de Peça ---")
    id_peca = input("ID da peça (ou ENTER para encerrar): ")
    if id_peca == "":
        break  # sai do loop se não digitar nada

    try:
        peso = float(input("Peso (g): "))
        cor = input("Cor: ").lower()
        comprimento = float(input("Comprimento (cm): "))
    except ValueError:
        print("❌ Dados inválidos. Tente novamente.")
        continue

    # Avaliação da peça
    if not (95 <= peso <= 105):
        pecas_reprovadas.append((id_peca, f"Peso fora do limite ({peso}g)"))
        continue
    if cor not in ("azul", "verde"):
        pecas_reprovadas.append((id_peca, f"Cor inválida ({cor})"))
        continue
    if not (10 <= comprimento <= 20):
        pecas_reprovadas.append((id_peca, f"Comprimento fora do limite ({comprimento}cm)"))
        continue

    # Se chegou até aqui, está aprovada
    pecas_aprovadas.append(id_peca)
    caixa_atual.append(id_peca)

    # Se a caixa atingir 10 peças, fecha e cria nova
    if len(caixa_atual) == 10:
        caixas.append(caixa_atual)
        caixa_atual = []

# Caso haja peças na última caixa, adiciona também
if caixa_atual:
    caixas.append(caixa_atual)

# --- Relatório Final ---
print("\n===== RELATÓRIO FINAL =====")
print(f"Total de peças aprovadas: {len(pecas_aprovadas)}")
print(f"Total de peças reprovadas: {len(pecas_reprovadas)}")
print(f"Quantidade de caixas utilizadas: {len(caixas)}\n")

if pecas_reprovadas:
    print("Peças reprovadas e motivos:")
    for id_peca, motivo in pecas_reprovadas:
        print(f" - ID {id_peca}: {motivo}")
