gastos = []

while True:
    print("\n--- CONTROLE DE GASTOS ---")
    print("1 - Adicionar gasto")
    print("2 - Ver gastos")
    print("3 - Ver total do mês")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        descricao = input("Digite o tipo de gasto (ex: comida, transporte): ")
        valor = float(input("Digite o valor: R$ "))

        gastos.append({
            "descricao": descricao,
            "valor": valor
        })

        print(" Gasto adicionado com sucesso!")

    elif opcao == "2":
        if len(gastos) == 0:
            print("Nenhum gasto registrado.")
        else:
            print("\n Lista de gastos:")
            for gasto in gastos:
                print(f"- {gasto['descricao']}: R$ {gasto['valor']:.2f}")

    elif opcao == "3":
        total = 0
        for gasto in gastos:
            total += gasto["valor"]

        print(f"\n Total gasto no mês: R$ {total:.2f}")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print(" Opção inválida, tente novamente.")