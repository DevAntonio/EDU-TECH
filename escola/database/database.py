import sqlite3 

DB_NAME = "escola.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabelas():
    con = conectar()
    cur = con.cursor()

    cur.execute("""
                    CREATE TABELE IF NOT EXISTS cursos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL
                    )
                """)
    
    cur.execute("""
                    CREATE TABLE IF NOT EXISTS turmas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        curso_id INTEGER,
                        FOREIGN KEY (curso_id) REFERENCES cursos(id)
                    )
                """)
    
    cur.execute("""
                    CREATE TABLE IF NOT EXISTS alunos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        turma_id INTEGER,
                        FOREIGN KEY (turma_id) REFERENCES turmas(id)
                    )
                """)
    
    con.commit()
    con.close()