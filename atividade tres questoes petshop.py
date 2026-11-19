import sqlite3

conexao = sqlite3.connect('petshop.db')
cursor = conexao.cursor()

print("Bem-vindo ao PetShop!")

cursor.execute('''
CREATE TABLE IF NOT EXISTS pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especie TEXT NOT NULL,
    tutor TEXT NOT NULL,
    idade INTEGER NOT NULL
)
''')
pets = [
    ('Bob', 'Cachorro', 'João Macedo', 5),
    ('Biscoito', 'Gato', 'Fernanda Rodrigues', 3),
    ('Joelma', 'Papagaio', 'Carlos Henriques', 2),
    ('Rodolfo', 'Coelho', 'Ana Carolina', 4),
    ('Bellinha', 'Hammester', 'Pedro Novaes', 3)
]
cursor.executemany("""
INSERT INTO pets (nome, especie, tutor, idade) VALUES (?, ?, ?, ?)
""", pets)

conexao.commit()


cursor.execute("SELECT * FROM pets WHERE especie =  ?", ("Cachorro",))
print(cursor.fetchall())

cursor.execute(
    "UPDATE pets SET tutor = ? WHERE id = ?", ("Maria Silva", 1)
)
conexao.commit()
print(cursor.execute("SELECT * FROM pets WHERE id = ?", (1,)).fetchone())

cursor.execute("DELETE FROM pets WHERE id = ?", (2,))
conexao.commit()
print(cursor.execute("DELETE FROM pets WHERE id = ?", (2,)).fetchone())
cursor.execute("SELECT * FROM pets")
pets = cursor.fetchall()

cursor.execute("""
DELETE FROM pets
 WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM pets
    GROUP BY nome, especie, tutor, idade
)
"""
)
