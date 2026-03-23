# Entrada das quatro notas bimestrais
try:
    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))
    n4 = float(input("Digite a 4ª nota: "))

    # Cálculo da média final
    media = (n1 + n2 + n3 + n4) / 4

    # Lógica para atribuição de Conceito
    if 9.0 <= media <= 10.0:
        conceito = "A"
    elif 7.5 <= media < 9.0:
        conceito = "B"
    elif 6.0 <= media < 7.5:
        conceito = "C"
    elif 4.0 <= media < 6.0:
        conceito = "D"
    else:
        conceito = "E"

    # Lógica para situação (Aprovado ou Reprovado)
    if conceito in ["A", "B", "C"]:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"

    # Exibição dos resultados conforme solicitado
    print("\n" + "="*30)
    print(f"NOTAS: {n1:.1f} | {n2:.1f} | {n3:.1f} | {n4:.1f}")
    print(f"MÉDIA FINAL: {media:.2f}")
    print(f"CONCEITO: {conceito}")
    print(f"SITUAÇÃO: {situacao}")
    print("="*30)

except ValueError:
    print("Erro: Por favor, digite apenas valores numéricos para as notas.")