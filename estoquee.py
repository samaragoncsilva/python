estoque={
    
    "feijao": 20,
    "arroz": 30,
    "cuscuz":40,
    "maizena": 30,
}

while True:
 produto=input("digite para ver se está no estoque[digite 'SAIR' se quiser sair ]:").lower().strip()
 
 if produto=='sair':
     print("saindo...")
     break
 
 if produto in estoque:
     print(f"{produto} está no estoque: {estoque[produto]} unidades")
     
 else:
     print(f"{produto} não está no estoque")