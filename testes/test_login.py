from validacao import validar_senha, validar_cpf, validar_celular

def test_validar_senha():
    assert validar_senha("Senha123") == True
    assert validar_senha("abc") == False

def test_validar_cpf():
    assert validar_cpf("12345678901") == True
    assert validar_cpf("123") == False

def test_validar_celular():
    assert validar_celular("81987654321") == True
    assert validar_celular("999") == False

