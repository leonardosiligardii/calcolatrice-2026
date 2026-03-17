from funzioni.somma import somma
import sys




def calculate_sum(num1, num2):
    """Calcola la somma di due numeri."""
    return somma(num1, num2)

def main():
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            risultato = calculate_sum(num1, num2)
            print(f"La somma di {num1} e {num2} è: {risultato}")
        except ValueError:
            print("Errore: inserisci numeri validi.")
    else:
        print("Benvenuto nella calcolatrice!")
        try:
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
            
            risultato = calculate_sum(num1, num2)
            
            print(f"La somma di {num1} e {num2} è: {risultato}")
        except ValueError:
            print("Errore: inserisci numeri validi.")

if __name__ == "__main__":
    main()