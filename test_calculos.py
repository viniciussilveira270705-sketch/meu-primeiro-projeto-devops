from calculos import soma, subtrai, multiplica, divide, potencia

def test_calculadora():
    assert soma(2, 2) == 4
    assert subtrai(10, 5) == 5
    assert multiplica(3, 3) == 9
    assert divide(10, 2) == 5
    assert potencia(2, 3) == 8
