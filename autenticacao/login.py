from db.conexao import conn, cursor
from validacao.regras import validar_senha, validar_cpf, validar_celular
import sqlite3

def cadastrar():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu email: ")
    celular = input("Digite seu celular: ")
    senha = input("Digite sua senha: ")

    if not validar_cpf(cpf):
        print("Erro: CPF deve conter exatamente 11 números.")
        return
    if not validar_celular(celular):
        print("Erro: Celular deve conter exatamente 11 números.")
        return
    if not validar_senha(senha):
        print("Erro: Senha deve conter entre 8 à 15 caracters, sendo letras e números.")
        return

    try:
        cursor.execute("INSERT INTO usuarios (nome, email, celular, cpf, senha) VALUES (?,?,?,?,?)",
                            (nome, email, celular, cpf, senha))
        conn.commit()
        print("Cadastro realizado com sucesso.")

    except sqlite3.IntegrityError:
        print("Erro: CPF já cadastrado.")

def login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    cursor.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, senha))
    usuario = cursor.fetchone()
    if usuario:
        print(f"Bem vindo {usuario[1]}!")
    else:
        print("Email ou senha incorretos.")

