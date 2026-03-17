from funzioni.somma import somma


def test01():
    num1 = 1
    num2 = 2
    risultato = somma(num1, num2)
    print(f"La somma di {num1} e {num2} è: {risultato}")

def test02():
    num1 = 1.0
    num2 = -2
    risultato = somma(num1, num2)
    print(f"La somma di {num1} e {num2} è: {risultato}")