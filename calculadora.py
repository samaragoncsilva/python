while True:
    print("---CALCULADORA---")
    print("1 - SOMAR")
    print("2 - SUBTRAIR")
    print("3 - MULTIPLICAR")
    print("4 - DIVIDIR")
    print("5 - SAIR")
    
    escolha = input("Escolha a opção (1-5): ")
    
    if escolha == '5':
        print("SAINDO...")
        break

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if escolha =='1':
            resultado=num1+num2
            print(f"resultado:{num1}+{num2} = {resultado}")
            
        elif escolha=='2':
            resultado=num1-num2
            print(f"resultado:{num1}-{num2} = {resultado}")
            
        elif escolha=='3':
            resultado=num1*num2
            print(f"resultado:{num1}x{num2} = {resultado}")
            
        elif escolha=='4':
            if num2==0:
                print("ERRO: DIVISÃO POR 0")
            else:
             resultado=num1/num2
            print(f"resultado:{num1}/{num2} = {resultado}")
            
        else:
            print("OPÇÃO INVALIDA")

    
    
    
    