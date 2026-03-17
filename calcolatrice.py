
from funzioni.somma import somma




def main():
    print("Benvenuto nella calcolatrice!")
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))
    
    risultato = somma(num1, num2)
    
    print(f"La somma di {num1} e {num2} è: {risultato}")

if __name__ == "__main__":
    main()
