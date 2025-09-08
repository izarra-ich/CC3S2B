import pytest
from app.app import summarize
        
# Generamos 3 datos para el test de summarize

# 1. caso normal: lista de strings convertibles a float
@pytest.fixture
def case_normal():
    return ["1", "2", "3"]
  
# 2. caso borde: lista vacía
@pytest.fixture
def case_empty():
    return []
  
# 3. caso error: lista con un elemento no convertible a float
@pytest.fixture
def case_error():
    return ["a", "2","3"]
  
def test_ok(case_normal):
    result = summarize(case_normal)
    # Debemos obtener count=3, sum=6.0, avg=2.0 en el formato de diccionario
    assert result == {"count": 3, "sum": 6.0, "avg": 2.0}
    
def test_empty(case_empty):
    # En este caso esperamos que lance ValueError por la lista vacía
    with pytest.raises(ValueError):
        summarize(case_empty) 
        
def test_non_numeric(case_error):
    # En este caso esperamos que lance ValueError por que el elemento "a" no es numérico
    with pytest.raises(ValueError):
        summarize(case_error) 
  
# Otros tests adicionales para llegar al 70% de cobertura

# Test de mensajes de error específicos para asegurar que son los correctos
def test_specific_error_messages():
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        summarize([])
    
    
# Para ejecutar los tests y generar el reporte de cobertura, usar:
# python -m pytest tests/test_app.py -v --cov=app.app --cov-report=term > coverage.txt test_empt