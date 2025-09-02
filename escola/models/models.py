from database.database import conectar

class Curso:
    def listar():
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM cursos ORDER BY id")
        
        rows = cur.fetchall()
        con.close()
        return rows
    
    def adicionar(nome:str):
        con = conectar()
        cur = con.cursor()

        cur.execute("INSERT INTO cursos (nome) VALUES (?)", (nome,))
        con.commit()
        con.close()

    def atualizar(id_:int, nome:str):
        con = conectar()
        cur = con.cursor()

        cur.execute("UPDATE cursos SET nome = ? WHERE id = ?", (nome, id_))
        con.commit()
        con.close()

    def deletar(id_:int):
        con = conectar()
        cur = con.cursor()

        cur.execute("DELETE FROM cursos WHERE id = ?", (id_,))
        con.commit()
        con.close()

class Turma:
    def listar():
        con = conectar()
        cur = con.cursor()
        cur.execute("""" SELECT t.id, t.nome, c.nome, COALESCE(c.nome, '') AS curso
                      FROM turmas t
                      LEFT JOIN cursos c ON c.id  = t.id """)
        
        rows = cur.fetchall()
        con.close()
        return rows
    
    def adicionar(nome:str, curso_id:int | None):
        con = conectar()
        cur = con.cursor()

        cur.execute("INSERT INTO turmas (nome, curso_id) VALUES (?, ?)", (nome, curso_id))
        con.commit()
        con.close()

    def atualizar(id_:int, nome:str, curso_id:int | None):
        con = conectar()
        cur = con.cursor()

        cur.execute("UPDATE turmas SET nome = ?, curso_id = ? WHERE id = ?", (nome, id_, curso_id))
        con.commit()
        con.close()

    def deletar(id_:int):
        con = conectar()
        cur = con.cursor()

        cur.execute("DELETE FROM turmas WHERE id = ?", (id_,))
        con.commit()
        con.close()

class Aluno:
    def listar():
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM alunos ORDER BY id")