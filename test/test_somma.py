from funzioni.somma import somma


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