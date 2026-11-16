from conversor import celsius_para_fahrenheit, fahrenheit_para_celsius


def test_celsius_para_fahrenheit_congelamento():
    assert celsius_para_fahrenheit(0) == 32.0


def test_celsius_para_fahrenheit_ebulicao():
    assert celsius_para_fahrenheit(100) == 212.0


def test_fahrenheit_para_celsius_congelamento():
    assert fahrenheit_para_celsius(32) == 0.0


def test_fahrenheit_para_celsius_ebulicao():
    assert fahrenheit_para_celsius(212) == 100.0
