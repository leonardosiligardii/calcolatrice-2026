from funzioni.somma import somma
from test.test_somma import test01, test02


# documentazione: https://github.com/Perteghella/2026-calcolatrice 
# creo anche dei file __init__ in ogni cartella che per delle versioni di python servono per collegare tutti i file tra loro dentro cartelle diverse, sono file nuovi
def main():
    print("Benvenuto nella calcolatrice!")
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))
    
    risultato = somma(num1, num2)
    
    print(f"La somma di {num1} e {num2} è: {risultato}")

if __name__ == "__main__":
    #main()
    test01()
    test02()