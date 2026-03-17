import subprocess
import sys
import os

def test_calcolatrice_integration():
    """Test di integrazione per calcolatrice.py con argomenti."""
    # Percorso al file calcolatrice.py
    script_path = os.path.join(os.path.dirname(__file__), '..', 'calcolatrice.py')
    
    # Test con argomenti 3 e 4, dovrebbe stampare "La somma di 3.0 e 4.0 è: 7.0"
    result = subprocess.run([sys.executable, script_path, '3', '4'], 
                          capture_output=True, text=True)
    
    assert result.returncode == 0
    assert "La somma di 3.0 e 4.0 è: 7.0" in result.stdout

def test_calculate_sum():
    """Test unitario per la funzione calculate_sum."""
    from calcolatrice import calculate_sum
    
    assert calculate_sum(1, 2) == 3
    assert calculate_sum(0, 0) == 0