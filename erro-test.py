def test_divisao_zero():
    resultado = 10 / 0
    assert resultado == 0

def test_assert_falso():
    assert False, "Este teste sempre falha de propósito"

def test_erro_variavel_nao_definida():
    assert valor_inexistente == 42

def test_string_incorreta():
    msg = "Olá mundo"
    assert msg == "Hello world"

def test_lista_vazia():
    lista = []
    assert lista[0] == 1

def test_sintaxe_simulada():
    eval("def erro(:)")
