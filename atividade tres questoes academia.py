import sqlite3

conexao = sqlite3.connect('academia.db')
cursor = conexao.cursor()

print("Bem-vindo à Academia!")

cursor.execute('''
CREATE TABLE IF NOT EXISTS membros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    plano TEXT NOT NULL,
    MENSALIDADE REAL NOT NULL,
    ativo INTEGER NOT NULL
)
''')

membros = [
    ('Alice', 'Trimestral', 150.00, 1),
    ('Paulo', 'Mensal', 85.00, 1),
    ('Carla', 'Mensal', 85.00, 1),
    ('Rafael', 'Anual', 590.00, 1),
    ('Fernanda', 'Trimestral', 150.00, 0)
]
cursor.executemany("""
INSERT INTO membros (nome, plano, MENSALIDADE, ativo) VALUES (?, ?, ?, ?)
""", membros)

conexao.commit()
print(membros)



cursor.execute("SELECT * FROM membros WHERE plano = ?", ("Anual",))
membros = cursor.fetchall()
for membro in membros:
    print(membro)

cursor.execute("UPDATE membros SET plano = ? WHERE MENSALIDADE = ?", ("Anual", 590.00))
              
conexao.commit()

cursor.execute("DELETE FROM membros WHERE ativo = ?", (0,))
conexao.commit()

receita_mensal = cursor.execute("SELECT SUM(MENSALIDADE) FROM membros").fetchone()[0]
receita_total = receita_mensal * 5 if receita_mensal else 0
print(f"A receita total da academia é: R${receita_total:.2f}")