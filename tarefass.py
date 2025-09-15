listasdecompras = []  

while True:
    print("\n*** MENU ***")
    print("1 - VER LISTA")
    print("2 - ADICIONAR ITEM")
    print("3 - REMOVER ITEM")
    print("4 - SAIR")

    try:
        opcao = input("Escolha a opção: ").strip()

        if opcao == "1":
            if len(listasdecompras) == 0:
                print("A lista está vazia.")
            else:
                print("Itens da lista:")
                for item in listasdecompras:
                    print(f"- {item}")

        elif opcao == "2":
            item = input("Digite o que quer adicionar: ").strip()
            listasdecompras.append(item)
            print(f"'{item}' adicionado à lista.")

        elif opcao == "3":
            item = input("Digite o item que quer remover: ").strip()
            if item in listasdecompras:
                listasdecompras.remove(item)
                print(f"'{item}' removido da lista.")
            else:
                print("O item não está na lista.")

        elif opcao == "4":
            print("Saindo do programa...")
            break

        else:
            print("OPÇÃO INVÁLIDA!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
