import tkinter as tk
from tkinter import ttk

from escola.models.models import Aluno, Turma

class AlunosView(tk.Frame):
    def __init__(self, master, voltar_callback):
        super().__init__(master, bg="#f0f0f0")
        self.pack(fill="both", expand=True)
        self.voltar_callback = voltar_callback
        self.sel_id = None

        tk.Label(self, text="Alunos", font=("Arial", 18, "bold"), bg="#f0f8ff").pack(pady=10)
        self.lista = tk.Listbox(self, width=54, height=12)
        self.lista.pack(pady=6)
        self.lista.bind("<<ListboxSelect>>", self.on_select)

        form = tk.Frame(self, bg="#f0f8ff").pack(pady=6)

        tk.Label(form, text="Nome:", bg="#f0f8ff").grid(row=0, column=0)
        self.ent_nome = tk.Entry(form, width=42)

        tk.Label(form, text="Turma:", bg="#f0f8ff").grid(row=0, column=0)
        self.cb_turmas = ttk.Combobox(form, width=42).grid(row=3, column=2, pady=4)

        box = tk.Frame(form, bg="#f0f8ff").pack(pady=8)
        tk.Button(box, text="Adicionar", width=12, command=self.adicionar).grid(row=0, column=0, pady=4)
        tk.Button(box, text="Atualizar", width=12, command=self.atualizar).grid(row=0, column=1, pady=4)
        tk.Button(box, text="Deletar", width=12, command=self.deletar).grid(row=0, column=2, pady=4)
        tk.Button(box, text="Voltar", width=12, command=self.voltar).grid(row=0, column=3, pady=4)

        self.carregar_turmas()
        self.carregar()

    def carregar_turmas(self):
       self.cb_turmas['values'] = [f"{t[0]} - {t[1]}" for t in Turma.listar()]

    def carregar(self):
        self.lista.delete(0, tk.END)  
        for a in Aluno.listar():
            self.lista.insert(tk.END, f"{a[0]} - {a[1]} | Turma: {a[2]}")
        self.sel_id = None
        self.ent_nome.delete(0, tk.END)
        self.cb_turmas.set("")

    def on_select(self, _):
        s = self.lista.curselection()
        if not s: return
        aluno = Aluno.listar()[s[0]] 
        self.sel_id = aluno[0]
        self.ent_nome.delete(0, tk.END)
        self.ent_nome.insert(0, aluno[1])