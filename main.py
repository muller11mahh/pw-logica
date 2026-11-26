

alunos = ["Pedro", "João", "Ana", "Davi", "Lucas"]

alunos.append("Erick")
print(alunos)

quantidade = len(alunos)
print(f"Temos {quantidade} alunos cadastrados.")

for aluno in alunos:
    print(f"Olá, {aluno}!")

    for contador in range(6):
        print(alunos[contador])
