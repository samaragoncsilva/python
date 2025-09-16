import random

alunos = []

for i in range(4):
    nome = input(f'Aluno {i+1}: ')
    alunos.append(nome)

sorteio = random.choice(alunos)
print(f'O aluno escolhido foi {sorteio}')
