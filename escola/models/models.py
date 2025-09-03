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

    def listar_alunos(turma_id):
        con = conectar()
        cur = con.cursor()

        cur.execute("SELECT id, nome FROM alunos WHERE turma_id = ?", (turma_id,))  
        dados = cur.fetchall()
        con.close()
        return dados

class Aluno:
    @staticmethod
    def listar():
        con = conectar()
        cur = con.cursor()
        cur.execute("""
                    SELECT a.id, a.nome, t.nome
                    from alunos a
                    LEFT JOIN turmas t ON t.turma_id = t.id
                    """)
        
        dados = cur.fetchall()
        con.close()
        return dados

    @staticmethod
    def adicionar(nome, turma_id = None):
        con = conectar()
        cur = con.cursor()

        cur.execute("INSERT INTO alunos(nome, turma_id) VALUES(?,?)", (nome, turma_id))
        con.commit()
        con.close()

    @staticmethod
    def atualizar(id_, nome, turma_id = None):
        con = conectar()
        cur = con.cursor()

        cur.execute("UPDATE alunos SET nome = ?, turma_id = ? WHERE id = ?", (nome, turma_id, id_))
        con.commit()
        con.close()

    @staticmethod
    def deletar(id_):
        con = conectar()
        cur = con.cursor()

        cur.execute("DELETE FROM alunos WHERE id = ?", (id_,))
        con.commit()
        con.close()