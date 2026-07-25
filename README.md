# Projeto Login em Python

Sistema simples de autenticação e cadastro de usuários desenvolvido em Python utilizando SQLite como banco de dados.
Projeto para demonstrar meu aprendizado em organização de projetos, uso de banco de dados e boas práticas de programação.

-----

## Funcionalidades
- Cadastro de novos usuários com validação de CPF, celular e senha (INSERT INTO)
- Login de usuários com verificação de email e senha (SELECT)
- Criação automática da tabela de usuários (CREATE TABLE IF NOT EXISTS)
- Estrutura modular com arquivos separados conexão, autenticação e validação

-----

## Tecnologias utilizadas
- Python 3.14.0
- SQLite 3.50.4 (Banco de dados leve e embutido)
- Virtualenv (venv) para ambiente isolado
- Pytest 9.1.1
- Regex para validação

-----

Estrutura do projeto
projeto_login/
main.py              # Menu inicial para login ou cadastro
autenticacao/
  -login.py          # Funções de cadastro e login
db/
  -conexao.py        # Conexão com o banco e criação da tabela
validacao/
  -regras.py         # Regras de validação (senha,CPF, celular)
tests/
  -test_login.py     # Testes automatizados das funções de validação
README.md            # Documentação do projeto

