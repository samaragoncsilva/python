from datetime import datetime

nome = str(input('Qual o seu nome?'))
ano_nasc = int(input('Qual o seu ano de nascimento?'))
ano_atual=datetime.now().year
idade=ano_atual-ano_nasc
if idade < 18:
    print(F'{nome}, você ainda tem {idade} anos, não tem idade suficiente para se alistar.')
elif idade == 18:
    print(f'{nome}, você já tem {idade} anos, precisa se alistar.')
elif idade > 18:
    print(f'{nome}, você já tem {idade} anos, está atrasado com o seu alistamento.')

