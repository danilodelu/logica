# Exibição do Menu
print("      MENU DE OPÇÕES")
print("1 - Opção 1")
print("2 - Opção 2")
print("3 - Opção 3")
print("4 - Sair")

# Entrada do usuário
opcao = input("Digite uma opção: ")

# Estrutura de decisão
if opcao == "1":
    print("Você selecionou a opção 1")
elif opcao == "2":
    print("Você selecionou a opção 2")
elif opcao == "3":
    print("Você selecionou a opção 3")
elif opcao == "4":
    print("Você selecionou sair")
else:
    print("Opção inválida!!!")

# Mensagem final (executada independente da opção escolhida)
print("Fim do programa!")