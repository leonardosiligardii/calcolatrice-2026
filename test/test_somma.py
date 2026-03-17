from funzioni.somma import somma
import pytest

def test_somma_positivi():
    num1 = 1
    num2 = 2
    risultato = somma(num1, num2)
    assert risultato == 3, f"Errore: la somma di {num1} e {num2} dovrebbe essere 3, ma è {risultato}"

def test_somma_negativi():
    num1 = 1.0
    num2 = -2
    risultato = somma(num1, num2)
    assert risultato == -1.0, f"Errore: la somma di {num1} e {num2} dovrebbe essere -1.0, ma è {risultato}"

def test_somma_con_zero():
    assert somma(0, 5) == 5
    assert somma(5, 0) == 5
    assert somma(0, 0) == 0

def test_somma_float():
    assert somma(1.5, 2.5) == 4.0
    assert somma(-1.5, 1.5) == 0.0

def test_somma_grandi_numeri():
    assert somma(1000000, 2000000) == 3000000
    assert somma(-1000000, 1000000) == 0

def test_somma_stringa_errore():
    with pytest.raises(ValueError, match="Impossibile sommare stringhe con numeri"):
        somma("hello", 5)
    with pytest.raises(ValueError, match="Impossibile sommare stringhe con numeri"):
        somma(5, "world")