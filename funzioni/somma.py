# Funzione somma

def somma(a, b):
    """
    Calcola la somma di due numeri.

    Args:
        a: Primo numero
        b: Secondo numero

    Returns:
        La somma di a e b

    Raises:
        ValueError: Se uno dei parametri è una stringa
    """
    if isinstance(a, str) or isinstance(b, str):
        raise ValueError("Impossibile sommare stringhe con numeri")
    return a + b