import sqlite3

try:
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    print("Banco conectado!")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        titulo TEXT NOT NULL,
        autor TEXT,
        ano INTEGER,
        disponivel INTEGER DEFAULT 1 CHECK (disponivel IN (0, 1))
    )
    """)

    #1-CREATE
    livros = [
    ("Dom Casmurro", "Machado de Assis", 1899, 1),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 1),
    ("Harry Potter", "J.K. Rowling", 1997, 1),
    ("A Culpa é das Estrelas", "John Green", 2012, 1),
    ("O Código Da Vinci", "Dan Brown", 2003, 1)
    ]

    cursor.executemany(
        """INSERT INTO livros (titulo, autor, ano, disponivel) VALUES (?, ?, ?, ?)""",
        livros
    )

    conexao.commit()

    #2-READ
    cursor.execute("Select * FROM livros")

    registros = cursor.fetchall()

    print("\n======LISTA DE LIVROS======")

    for livro in registros:
        print(livro)

    #3-UPDATE
    cursor.execute("""
    UPDATE livros SET disponivel = 0 WHERE id = 1
    """)

    conexao.commit()

    cursor.execute("Select * FROM livros")
    
    registros = cursor.fetchall()
    
    print("\n======LISTA DE LIVROS======")
    
    for livro in registros:
        print(livro)

    #4-DELETE
    cursor.execute("""
    DELETE FROM livros WHERE id = 2
    """)

    conexao.commit()

    cursor.execute("Select * FROM livros")
    
    registros = cursor.fetchall()
    
    print("\n======LISTA DE LIVROS======")
    
    for livro in registros:
        print(livro)

    #5-EXTRA
    print("\n===== LIVROS PUBLICADOS DEPOIS DE 2000 =====")

    cursor.execute("""
    SELECT * FROM livros WHERE ano > 2000
    """)

    resultado = cursor.fetchall()

    if resultado:
        for livro in resultado:
            print(f"Título: {livro[1]}")
            print(f"Autor: {livro[2]}")
            print(f"Ano: {livro[3]}")

except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)