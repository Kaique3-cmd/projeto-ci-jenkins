import pytest
from calculadora import somar, dividir


def test_somar_numeros_positivos():
    assert somar(10, 5) == 15


def test_dividir_valores_validos():
    assert dividir(20, 4) == 5


def test_dividir_por_zero_deve_falhar():
    with pytest.raises(ValueError):
        dividir(10, 0)