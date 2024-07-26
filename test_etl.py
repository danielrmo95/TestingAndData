# test_operaciones.py
import pytest
from operaciones import sumar
import time

def test_sumar():
    # Caso de prueba 1: Suma de enteros
    resultado = sumar(2, 3)
    assert resultado == 5

    # Caso de prueba 2: Suma de enteros negativos
    resultado = sumar(-1, 1)
    assert resultado == 0

    # Caso de prueba 3: Suma de ceros
    resultado = sumar(0, 0)
    assert resultado == 0

    # Caso de prueba 4: Suma de números decimales
    resultado = sumar(2.5, 1.5)
    assert resultado == 4.0

    # Caso de prueba 5: Suma de cadena y número (debería lanzar un TypeError)
    try:
        resultado = sumar("2", 1)
        assert False  # El caso de prueba debería fallar si no se lanza la excepción
    except TypeError as e:assert str(e) == 'can only concatenate str (not "int") to str'

    # Puedes agregar más casos de prueba según sea necesario
