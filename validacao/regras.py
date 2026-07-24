import re

def validar_senha(senha):
    padrao = r'^[a-zA-Z\d]{8,15}$'
    return re.match(padrao, senha) is not None

def validar_cpf(cpf):
    padrao = r'^\d{11}$'
    return re.match(padrao, cpf) is not None

def validar_celular(celular):
    padrao = r'^\d{11}$'
    return re.match(padrao, celular) is not None

