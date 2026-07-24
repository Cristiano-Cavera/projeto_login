from autenticacao.login import cadastrar, login

print("Você tem cadastro? Digite 1")
print("Você não tem cadastro? Digite 2")

opcao = input("Escolha: ")

if opcao == "1":
    login()
elif opcao == "2":
    cadastrar()
else:
    print("Opção invalida")
