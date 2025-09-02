print("SEJA BEM-VINDO(A) À HAMBURGUERIA BURGUERMANIA")
print("Veja o nosso cardápio:\n")

print("HAMBÚRGUERES")
print("1. X-SALADA         - R$ 7,00")
print("2. CHEESEBURGUER    - R$ 10,00")
print("3. BACON BURGUER    - R$ 15,00")
print("4. X-TUDO           - R$ 20,00\n")

print("BEBIDAS")
print("5. CERVEJA SKOL 350ML    - R$ 4,99")
print("6. COCA-COLA  350ML      - R$ 3,00")
print("7. FANTA  350ML          - R$ 2,00")
print("8. GUARANÁ  350ML        - R$ 2,00\n")

print("ACOMPANHAMENTOS")
print("9. BATATA FRITA 100G    - R$ 10,90")
print("10. FRANGO EMPANADO 100G- R$ 12,00\n")

print("Digite o número do item (0 para encerrar)\n")


total = 0
pedidos = []


while True:
    escolha = input("Escolha o número do item: ")

    if escolha == "0":
        break

    if escolha == "1":
        pedidos.append("X-SALADA - R$ 7,00") # usei append() para colocar cada item escolhido pelo cliente na lista
        total += 7.00
    elif escolha == "2":
        pedidos.append("CHEESEBURGUER - R$ 10,00")
        total += 10.00
    elif escolha == "3":
        pedidos.append("BACON BURGUER - R$ 15,00")
        total += 15.00
    elif escolha == "4":
        pedidos.append("X-TUDO - R$ 20,00")
        total += 20.00
    elif escolha == "5":
        pedidos.append("CERVEJA SKOL 350ML  - R$ 4,99")
        total += 4.99
    elif escolha == "6":
        pedidos.append("COCA-COLA 350ML  - R$ 3,00")
        total += 3.00
    elif escolha == "7":
        pedidos.append("FANTA 350ML  - R$ 2,00")
        total += 2.00
    elif escolha == "8":
        pedidos.append("GUARANÁ 350ML  - R$ 2,00")
        total += 2.00
    elif escolha == "9":
        pedidos.append("BATATA FRITA 100G  - R$ 10,90")
        total += 10.90
    elif escolha == "10":
        pedidos.append("FRANGO EMPANADO 100G  - R$ 12,00")
        total += 12.00
    else:
        print("Opção inválida, tente novamente.")


print("\n=== PEDIDOS ===")
for item in pedidos:
    print(item)

print(f"\nTOTAL: R$ {total:.2f}")
print("Obrigado pelo seu pedido!")
