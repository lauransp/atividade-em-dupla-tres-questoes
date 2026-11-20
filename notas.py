import sqlite3

try:
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    print("Banco conectado!")

    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS boletim (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno TEXT NOT NULL,
    disciplina TEXT,
    nota1 REAL,
    nota2 REAL
    )
    """)

    #1-CREATE
    alunos = [
        ("Ana", "Matemática", 8.0, 9.0),
        ("Carlos", "Matemática", 6.0, 5.0),
        ("Mariana", "Português", 7.0, 8.0),
        ("Pedro", "Português", 4.0, 6.0),
        ("João", "História", 9.0, 10.0)
    ]

    cursor.executemany("""
    INSERT INTO boletim (aluno, disciplina, nota1, nota2) VALUES (?, ?, ?, ?)
    """, alunos
    )

    conexao.commit()

    #2-READ
    cursor.execute("SELECT * FROM boletim")

    registros = cursor.fetchall()

    print("\n======BOLETIM ESCOLAR======")

    for aluno in registros:
        print(aluno)

    #3-UPDATE
    cursor.execute("""
    UPDATE boletim SET nota2 = ? WHERE aluno = ?
    """, (8.0, "Carlos")
    )

    conexao.commit()

    cursor.execute("SELECT * FROM boletim")

    registros = cursor.fetchall()

    print("\n======BOLETIM ESCOLAR======")
    print("======Nota atualizada======")

    for aluno in registros:
        print(aluno)

    #4-DELETE
    cursor.execute("""
    DELETE FROM boletim WHERE aluno = ?
    """, ("Pedro",)
    )

    conexao.commit()
    
    cursor.execute("SELECT * FROM boletim")
    
    registros = cursor.fetchall()
    
    print("\n======BOLETIM ESCOLAR======")
    print("======Aluno excluído======")
    
    for aluno in registros:
        print(aluno)

    #5-EXTRA
    cursor.execute("SELECT * FROM boletim")

    registros = cursor.fetchall()

    print("\n======RESULTADO FINAL======")

    for aluno in registros:
        nome = aluno[1]
        disciplina = aluno[2]
        nota1 = aluno[3]
        nota2 = aluno[4]

        media = (nota1 + nota2) / 2

        if media >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        print("------------------------")
        print("Aluno: ", nome)
        print("Disciplina: ", disciplina)
        print("Média: ", media)
        print("Situação", situacao)

except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)